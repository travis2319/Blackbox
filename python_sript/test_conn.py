import obd

connection = obd.OBD("/dev/ttyACM0") # create connection with USB 0

print(connection)

cmd = obd.commands.COOLANT_TEMP

response = connection.query(cmd)

print(response.value)



cmd = obd.commands.SPEED

response = connection.query(cmd)

print(response.value)

print(response.value.to("mph"))




# ports = obd.scan_serial()      # return list of valid USB or RF ports
# print ports                    # ['/dev/ttyUSB0', '/dev/ttyUSB1']
# connection = obd.OBD(ports[0]) # connect to the first port in the list



# connection = obd.OBD() # auto connect

# # OR

# OR