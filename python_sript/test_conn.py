import obd
import pandas as pd

# connection = obd.OBD("/dev/ttyACM0") # create connection with USB 0

dis={"a":[],"b":[]}

# print(connection)

# cmd = obd.commands.COOLANT_TEMP

# response = connection.query(cmd)

# print(response.value)
dis["a"].append("response value")


# cmd = obd.commands.SPEED

# response = connection.query(cmd)

# print(response.value)

# print(response.value.to("mph"))
dis["b"].append("response value")

d=pd.DataFrame(dis)
d.to_csv("Test9.csv")

