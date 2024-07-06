# # import threading
# import time
# from blackbox import run_obd, run_gps
# import logging

# # Setup logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def check_internet_and_upload():
#     while True:
#         try:
#             upload_data()
#         except Exception as e:
#             logging.error(f"Error during data upload: {e}")
#         time.sleep(60)  # Check every 60 seconds

# if __name__ == "__main__":
#     # Create threads for OBD and GPS handlers
#     obd_thread = threading.Thread(target=run_obd)
#     gps_thread = threading.Thread(target=run_gps)

#     # Start both threads
#     obd_thread.start()
#     gps_thread.start()

#     # Wait for both threads to complete
#     obd_thread.join()
#     gps_thread.join()

#     print("OBD and GPS handlers have finished execution.")

import pandas as pd
import numpy as np
import obd
import time
# import requests
# import serial
# # import pynmea2 # type: ignore
# import signal
# import sys
import matplotlib
import datetime


# Print library versions
print(f"pandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")
print(f"obd version: {obd.__version__}")
print(f"matplotlib version: {matplotlib.__version__}")

# Print current time
print(time.time())
print(f"Time: {datetime.datetime.now().ctime()}")

# # Setup OBD connection
# obd_connector = "/dev/ttyACM0"
# print(obd_connector)

# connection = obd.Async(obd_connector)
# df = pd.DataFrame(columns=["Start_Time", "SPEED", "Coolant Temp", "Engine Load", "Throttle_pos_b", "End_Time"])

# def new_rpm(responses):
#     start_timestamp = time.time()
#     speed = responses.value
#     print(speed)
#     df.loc[len(df)] = [start_timestamp, speed, np.nan, np.nan, np.nan, np.nan]

# def coolant_temp(responses):
#     temp = responses.value
#     print(temp)
#     df.loc[len(df) - 1, "Coolant Temp"] = temp

# def engine_load(responses):
#     load = responses.value
#     print(load)
#     df.loc[len(df) - 1, "Engine Load"] = load

# def throttle_pos(responses):
#     end_timestamp = time.time()
#     throttle = responses.value
#     print(throttle)
#     df.loc[len(df) - 1, "Throttle_pos_b"] = throttle
#     df.loc[len(df) - 1, "End_Time"] = end_timestamp

# connection.watch(obd.commands.SPEED, callback=new_rpm)
# connection.watch(obd.commands.COOLANT_TEMP, callback=coolant_temp)
# connection.watch(obd.commands.ENGINE_LOAD, callback=engine_load)
# connection.watch(obd.commands.THROTTLE_POS_B, callback=throttle_pos)
# connection.start()

# # Setup Google Apps Script URL
# base_url = "https://script.google.com/macros/s/AKfycbwVR6GLTTL99a4dFJazRhK-0fBl9YMY6kkyGrdJoYbXsVs_bp8xJo_tQgKcxvoMO46CLw/exec"

# # Setup GPS
# port = "/dev/ttyAMA0"

# # Signal handler for graceful shutdown
# def signal_handler(sig, frame):
#     print("Stopping...")
#     connection.stop()
#     df.to_csv('async_log.csv', mode='a')
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)

# # Main loop
# try:
#     with serial.Serial(port, baudrate=9600, timeout=0.5) as ser:
#         dataout = pynmea2.NMEAStreamReader()
#         while True:
#             newdata = ser.readline().decode().strip()
#             if newdata and newdata[0:6] == "$GPRMC":
#                 try:
#                     newmsg = pynmea2.parse(newdata)
#                     lat = newmsg.latitude
#                     lng = newmsg.longitude
#                     gps = f"Latitude={lat} and Longitude={lng}"
#                     print(gps)
#                 except pynmea2.ParseError as e:
#                     print(f"Error parsing NMEA data: {e}")

#             # Sending data to Google Sheets
#             for index, row in df.iterrows():
#                 speed = row["SPEED"]
#                 coolant_temp = row["Coolant Temp"]
#                 engine_load = row["Engine Load"]

#                 full_url = f"{base_url}?value1={coolant_temp}&value2={speed}&value3={engine_load}"

#                 response = requests.get(full_url)
#                 if response.status_code == 200:
#                     print(f"Data for row {index + 1} successfully sent to Google Sheets")
#                 else:
#                     print(f"Failed to send data for row {index + 1}. Status code: {response.status_code}")
#                     print(f"Response content: {response.text}")

# except serial.SerialException as e:
#     print(f"Error opening serial port: {e}")

# except Exception as e:
#     print(f"Unexpected error: {e}")

# finally:
#     print("Saving data...")
#     df.to_csv('async_log.csv', mode='a')
#     print("All data saved.")
