# import pandas as pd
# import numpy as np
# import obd
# import time
# import requests
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

# def run_obd():
#     obd_connector = "/dev/ttyACM0"
#     print(obd_connector)
#     connection = obd.Async(obd_connector)
    
    
#     print("obd working")
#     connection.watch(obd.commands.SPEED, callback=new_rpm)
#     connection.watch(obd.commands.COOLANT_TEMP, callback=coolant_temp)
#     connection.watch(obd.commands.ENGINE_LOAD, callback=engine_load)
#     connection.watch(obd.commands.THROTTLE_POS_B, callback=throttle_pos)
#     connection.start()

#     time.sleep(20)
#     connection.stop()

#     print(df)
#     df.to_csv('async_log.csv', mode='a')
    
#     # Base URL of your Google Apps Script web app
#     base_url = "https://script.google.com/macros/s/AKfycbwVR6GLTTL99a4dFJazRhK-0fBl9YMY6kkyGrdJoYbXsVs_bp8xJo_tQgKcxvoMO46CLw/exec"

#     # Loop through each row in the DataFrame
#     for index, row in df.iterrows():
#         # Extract values from the current row
#         speed = row["SPEED"]
#         coolant_temp = row["Coolant Temp"]
#         engine_load = row["Engine Load"]

#         # Construct the full URL with query parameters
#         full_url = f"{base_url}?value1={coolant_temp}&value2={speed}&value3={engine_load}"

#         # Send the GET request
#         response = requests.get(full_url)

#         # Check if the request was successful
#         if response.status_code == 200:
#             print(f"Data for row {index + 1} successfully sent to Google Sheets")
#         else:
#             print(f"Failed to send data for row {index + 1}. Status code: {response.status_code}")
#             print(f"Response content: {response.text}")

#     print("All data sent. DataFrame contents:")
#     print(df)

import pandas as pd
import numpy as np
import obd
import time
import requests
from obd import OBDStatus

# Initialize DataFrame
def initialize_dataframe():
    return pd.DataFrame(columns=["Start_Time", "SPEED", "Coolant Temp", "Engine Load", "Throttle_pos_b", "End_Time"])
# Callback functions
def new_rpm(responses):
    start_timestamp = time.time()
    speed = responses.value if responses.value is not None else 0
    print(speed)
    df.loc[len(df)] = [start_timestamp, speed, np.nan, np.nan, np.nan, np.nan]

def coolant_temp(responses):
    temp = responses.value if responses.value is not None else 0
    print(temp)
    df.loc[len(df) - 1, "Coolant Temp"] = temp

def engine_load(responses):
    load = responses.value if responses.value is not None else 0
    print(load)
    df.loc[len(df) - 1, "Engine Load"] = load

def throttle_pos(responses):
    end_timestamp = time.time()
    throttle = responses.value if responses.value is not None else 0
    print(throttle)
    df.loc[len(df) - 1, "Throttle_pos_b"] = throttle
    df.loc[len(df) - 1, "End_Time"] = end_timestamp

# OBD connection setup
def setup_obd_connection():
    obd_connector = "/dev/ttyACM0"
    print(obd_connector)
    connection = obd.Async(obd_connector)
    print("obd connector working in setup_obd_connection function")
    return connection

# Watch OBD commands
def watch_obd_commands(connection):
    connection.watch(obd.commands.SPEED, callback=new_rpm)
    connection.watch(obd.commands.COOLANT_TEMP, callback=coolant_temp)
    connection.watch(obd.commands.ENGINE_LOAD, callback=engine_load)
    connection.watch(obd.commands.THROTTLE_POS_B, callback=throttle_pos)

# Run OBD connection
def run_obd_connection(connection):
    connection.start()
    time.sleep(20)
    connection.stop()

# Save data to CSV
def save_to_csv(df):
    df.to_csv('async_log.csv', mode='a')

# Send data to Google Sheets
def send_to_google_sheets(df):
    base_url = "https://script.google.com/macros/s/AKfycbwVR6GLTTL99a4dFJazRhK-0fBl9YMY6kkyGrdJoYbXsVs_bp8xJo_tQgKcxvoMO46CLw/exec"

    for index, row in df.iterrows():
        speed = row["SPEED"]
        coolant_temp = row["Coolant Temp"]
        engine_load = row["Engine Load"]

        full_url = f"{base_url}?value1={coolant_temp}&value2={speed}&value3={engine_load}"

        response = requests.get(full_url)

        if response.status_code == 200:
            print(f"Data for row {index + 1} successfully sent to Google Sheets")
        else:
            print(f"Failed to send data for row {index + 1}. Status code: {response.status_code}")
            print(f"Response content: {response.text}")

    print("All data sent. DataFrame contents:")
    print(df)

def run_obd():
    global df
    df = initialize_dataframe()
    connection = setup_obd_connection()
    print(connection.status() == OBDStatus.NOT_CONNECTED)
    print(connection.status() == OBDStatus.OBD_CONNECTED)
    print(connection.status() == OBDStatus.CAR_CONNECTED)
    if(connection.status() == OBDStatus.CAR_CONNECTED):
        print("car connected!!")
        
        watch_obd_commands(connection)
        run_obd_connection(connection)
        save_to_csv(df)
        send_to_google_sheets(df)
    else:
        print("not connected!!")