package main

import (
    "database/sql"
    "encoding/json"
    "fmt"
    "log"
    "net"
    "strconv"
    // "github.com/gofiber/fiber/v2"
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
    Timestamp float64 `json:"timestamp"`
    Latitude  float64 `json:"latitude"`
    Longitude float64 `json:"longitude"`
    Altitude  float32 `json:"altitude"`
}

func (gpsData *GpsData) UnmarshalJSON(data []byte) error {
    var aux struct {
        Timestamp string `json:"timestamp"`
        Latitude  float64 `json:"latitude"`
        Longitude float64 `json:"longitude"`
        Altitude  float32 `json:"altitude"`
    }

    err := json.Unmarshal(data, &aux)
    if err!= nil {
        return err
    }

    timestampFloat, err := strconv.ParseFloat(aux.Timestamp, 64)
    if err!= nil {
        return err
    }

    gpsData.Timestamp = timestampFloat
    gpsData.Latitude = aux.Latitude
    gpsData.Longitude = aux.Longitude
    gpsData.Altitude = aux.Altitude

    return nil
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
            buf := make([]byte, 1024)
            n, addr, err := udpConn.ReadFromUDP(buf)
            if err != nil {
                log.Println("Error reading from UDP: ", err)
                continue
            }

            var gpsData GpsData
            err = json.Unmarshal(buf[:n], &gpsData)
            if err != nil {
                log.Println("Error unmarshalling JSON: ", err)
                continue
            }

            log.Printf("Received data from %s: %+v\n", addr, gpsData)

            insertQuery := `INSERT INTO public.gps_log (timestamp, latitude, longitude, altitude)
                            VALUES ($1, $2, $3, $4)`
            _, err = db.Exec(insertQuery, gpsData.Timestamp, gpsData.Latitude, gpsData.Longitude, gpsData.Altitude)
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
    
