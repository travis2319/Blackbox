import obd

connection = obd.Async() # same constructor as 'obd.OBD()'; see below.

connection.watch(obd.commands.RPM) # keep track of the RPM

connection.start() # start the async update loop

print connection.query(obd.commands.RPM) # non-blocking, returns immediately