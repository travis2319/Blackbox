package main

import (
    "database/sql"
    "encoding/binary"
    "fmt"
    "log"
    "net"
    "math"
    _ "github.com/lib/pq" // PostgreSQL driver
)

const (
    host     = "localhost"
    port     = 5432
    user     = "postgres"
    password = "admin"
    dbname   = "adam"
    udpPort  = 3000
)

type GpsData struct {
    Timestamp float64
    Latitude  float64
    Longitude float64
}

func main() {
    // Set up PostgreSQL connection
    psqlInfo := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
        host, port, user, password, dbname)

    db, err := sql.Open("postgres", psqlInfo)
    if err != nil {
        log.Fatal("Error connecting to the database: ", err)
    }
    defer db.Close()

    err = db.Ping()
    if err != nil {
        log.Fatal("Error pinging the database: ", err)
    }

    fmt.Println("Successfully connected to the database!")

    // Start UDP listener
    udpAddr, err := net.ResolveUDPAddr("udp", fmt.Sprintf(":%d", udpPort))
    if err != nil {
        log.Fatal("Error resolving UDP address: ", err)
    }

    udpConn, err := net.ListenUDP("udp", udpAddr)
    if err != nil {
        log.Fatal("Error listening on UDP: ", err)
    }
    defer udpConn.Close()

    fmt.Printf("UDP server listening on port %d\n", udpPort)

    // Use a channel to keep the main goroutine running
    done := make(chan bool)

    go func() {
        for {
            buf := make([]byte, 24) // 8 bytes for timestamp, 8 for latitude, 8 for longitude
            n, addr, err := udpConn.ReadFromUDP(buf)
            if err != nil {
                log.Println("Error reading from UDP: ", err)
                continue
            }

            if n != 24 {
                log.Printf("Received unexpected number of bytes: %d\n", n)
                continue
            }

            var gpsData GpsData
            gpsData.Timestamp = math.Float64frombits(binary.BigEndian.Uint64(buf[0:8]))
            gpsData.Latitude = math.Float64frombits(binary.BigEndian.Uint64(buf[8:16]))
            gpsData.Longitude = math.Float64frombits(binary.BigEndian.Uint64(buf[16:24]))

            log.Printf("Received data from %s: %+v\n", addr, gpsData)

            insertQuery := `INSERT INTO public.gps_log (timestamp, latitude, longitude)
                            VALUES ($1, $2, $3)`
            _, err = db.Exec(insertQuery, gpsData.Timestamp, gpsData.Latitude, gpsData.Longitude)
            if err != nil {
                log.Println("Error inserting data: ", err)
            } else {
                log.Println("Data inserted successfully!")
            }
        }
    }()

    // Keep the main goroutine running
    <-done
}