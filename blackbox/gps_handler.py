# import serial
# import pynmea2
# import logging

# port = "/dev/ttyAMA0"

# def run_gps():
#     logging.info("GPS module started")
#     try:
#         with serial.Serial(port, baudrate=9600, timeout=0.5) as ser:
#             dataout = pynmea2.NMEAStreamReader()
#             while True:
#                 newdata = ser.readline().decode().strip()
#                 if newdata and newdata[0:6] == "$GPRMC":
#                     try:
#                         newmsg = pynmea2.parse(newdata)
#                         lat = newmsg.latitude
#                         lng = newmsg.longitude
#                         gps = f"Latitude={lat} and Longitude={lng}"
#                         logging.info(gps)
#                     except pynmea2.ParseError as e:
#                         logging.error(f"Error parsing NMEA data: {e}")
#     except serial.SerialException as e:
#         logging.error(f"Error opening serial port: {e}")

# # import serial
# # import pynmea2

# # port = "/dev/ttyAMA0"

# def run_gps():
#     print("gps working")
# #     try:
# #         with serial.Serial(port, baudrate=9600, timeout=0.5) as ser:
# #             dataout = pynmea2.NMEAStreamReader()
# #             while True:
# #                 newdata = ser.readline().decode().strip()
# #                 if newdata and newdata[0:6] == "$GPRMC":
# #                     try:
# #                         newmsg = pynmea2.parse(newdata)
# #                         lat = newmsg.latitude
# #                         lng = newmsg.longitude
# #                         gps = f"Latitude={lat} and Longitude={lng}"
# #                         print(gps)
# #                     except pynmea2.ParseError as e:
# #                         print(f"Error parsing NMEA data: {e}")
# #     except serial.SerialException as e:
# #         print(f"Error opening serial port: {e}")

import serial
import pynmea2

def get_gps_location():
    # Initialize the serial connection to the GPS module
    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)  # Adjust port as needed
    
    while True:
        try:
            # Read a line from the GPS module
            line = ser.readline().decode('ascii', errors='replace')
            
            # Check if it's a GPGGA sentence (Global Positioning System Fix Data)
            if line.startswith('$GPGGA'):
                # Parse the NMEA sentence
                msg = pynmea2.parse(line)
                
                # Extract latitude and longitude
                lat = msg.latitude
                lon = msg.longitude
                
                # Close the serial connection
                ser.close()
                
                # Return the location
                return lat, lon
                
        except serial.SerialException as e:
            print(f"Device error: {e}")
            return None
        except pynmea2.ParseError as e:
            print(f"Parse error: {e}")
            continue
        except KeyboardInterrupt:
            print("Stopping...")
            ser.close()
            return None

# Get the location once
location = get_gps_location()

if location:
    lat, lon = location
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Failed to get GPS location")

#######################################################################################

# import serial
# import pynmea2
# import time
# from pyubx2 import UBXMessage

# def set_rate_5hz(serial_port):
#     # Create a UBX-CFG-RATE message for 5Hz
#     msg = UBXMessage('CFG', 'CFG-RATE', payload=b'\xC8\x00\x01\x00\x01\x00')
    
#     # Send the message
#     serial_port.write(msg.serialize())
#     time.sleep(1)  # Give the module a moment to process the command

# def get_gps_data(duration_seconds=10):
#     # Initialize the serial connection to the GPS module
#     ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)  # Adjust port as needed
    
#     try:
#         # Set update rate to 5Hz
#         set_rate_5hz(ser)
        
#         start_time = time.time()
#         while time.time() - start_time < duration_seconds:
#             try:
#                 # Read a line from the GPS module
#                 line = ser.readline().decode('ascii', errors='replace')
                
#                 # Check if it's a GPGGA sentence (Global Positioning System Fix Data)
#                 if line.startswith('$GPGGA'):
#                     # Parse the NMEA sentence
#                     msg = pynmea2.parse(line)
                    
#                     # Extract latitude, longitude, and time
#                     lat = msg.latitude
#                     lon = msg.longitude
#                     gps_time = msg.timestamp
                    
#                     print(f"Time: {gps_time}, Latitude: {lat}, Longitude: {lon}")
                    
#             except pynmea2.ParseError as e:
#                 print(f"Parse error: {e}")
#                 continue
#             except KeyboardInterrupt:
#                 print("Stopping...")
#                 break
    
#     except serial.SerialException as e:
#         print(f"Device error: {e}")
#     finally:
#         ser.close()

# # Get GPS data for 10 seconds
# get_gps_data(10)

##########################################################################

# import asyncio
# import csv
# import time
# from motor.motor_asyncio import AsyncIOMotorClient
# import obd
# import gps

# # Configuration
# OBD_PORT = '/dev/ttyUSB0'  # Adjust as needed
# GPS_PORT = '/dev/ttyUSB1'  # Adjust as needed
# MONGO_URI = 'mongodb://localhost:27017'
# DB_NAME = 'car_blackbox'
# BATCH_SIZE = 10
# FLUSH_INTERVAL = 5  # seconds

# # Globals
# obd_data = []
# gps_data = []

# async def capture_obd():
#     connection = obd.Async(OBD_PORT)
    
#     def new_speed(s):
#         obd_data.append({'timestamp': time.time(), 'speed': s.value.magnitude})
    
#     def new_rpm(r):
#         obd_data.append({'timestamp': time.time(), 'rpm': r.value.magnitude})
    
#     connection.watch(obd.commands.SPEED, callback=new_speed)
#     connection.watch(obd.commands.RPM, callback=new_rpm)
#     connection.start()
    
#     while True:
#         await asyncio.sleep(0.1)

# async def capture_gps():
#     gpsd = gps.gps(mode=gps.WATCH_ENABLE)
    
#     while True:
#         report = gpsd.next()
#         if report['class'] == 'TPV':
#             gps_data.append({
#                 'timestamp': time.time(),
#                 'latitude': getattr(report, 'lat', 0.0),
#                 'longitude': getattr(report, 'lon', 0.0)
#             })
#         await asyncio.sleep(0.1)

# async def flush_to_csv():
#     while True:
#         if obd_data:
#             with open('obd.csv', 'a', newline='') as f:
#                 writer = csv.DictWriter(f, fieldnames=['timestamp', 'speed', 'rpm'])
#                 writer.writerows(obd_data)
#             obd_data.clear()
        
#         if gps_data:
#             with open('gps.csv', 'a', newline='') as f:
#                 writer = csv.DictWriter(f, fieldnames=['timestamp', 'latitude', 'longitude'])
#                 writer.writerows(gps_data)
#             gps_data.clear()
        
#         await asyncio.sleep(FLUSH_INTERVAL)

# async def send_to_database():
#     client = AsyncIOMotorClient(MONGO_URI)
#     db = client[DB_NAME]
    
#     while True:
#         if len(obd_data) >= BATCH_SIZE:
#             await db.obd_collection.insert_many(obd_data[:BATCH_SIZE])
#             del obd_data[:BATCH_SIZE]
        
#         if len(gps_data) >= BATCH_SIZE:
#             await db.gps_collection.insert_many(gps_data[:BATCH_SIZE])
#             del gps_data[:BATCH_SIZE]
        
#         await asyncio.sleep(0.1)

# async def main():
#     tasks = [
#         asyncio.create_task(capture_obd()),
#         asyncio.create_task(capture_gps()),
#         asyncio.create_task(flush_to_csv()),
#         asyncio.create_task(send_to_database())
#     ]
#     await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Stopping...")