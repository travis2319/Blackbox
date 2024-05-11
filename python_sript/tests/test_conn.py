import obd
import pandas as pd

# connection = obd.OBD("/dev/ttyACM0") # create connection with USB 0

# print(connection)

# cmd = obd.commands.COOLANT_TEMP

# response = connection.query(cmd)

# print(response.value)


# cmd = obd.commands.SPEED

# response = connection.query(cmd)

# print(response.value)

# print(response.value.to("mph"))

# data of Player and their performance
data = {
    'Name': ['Hardik', 'Pollard', 'Bravo'],
    'Run': [50, 63, 15],
    'Wicket': [0, 2, 3],
    'Catch': [4, 2, 1]
}

# Make data frame of above datas
df = pd.DataFrame(data)

# append data frame to CSV file
df.to_csv('GFG.csv', mode='a', index=False, header=False)

# print message
print("Data appended successfully.")
