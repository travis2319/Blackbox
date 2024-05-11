import obd

connection = obd.Async("/dev/ttyACM0")

connection.watch(obd.commands.SPEED)

connection.start()

print (connection.query(obd.commands.SPEED))