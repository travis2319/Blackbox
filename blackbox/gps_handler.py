# import serial
# import pynmea2

# port = "/dev/ttyAMA0"

def run_gps():
    print("gps working")
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
#                         print(gps)
#                     except pynmea2.ParseError as e:
#                         print(f"Error parsing NMEA data: {e}")
#     except serial.SerialException as e:
#         print(f"Error opening serial port: {e}")

