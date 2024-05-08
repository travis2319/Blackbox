import obd
import time

connection = obd.Async("/dev/ttyACM0")
print(connection)
# a callback that prints every new value to the console
def new_rpm(r):
    print (r.value)

connection.watch(obd.commands.SPEED, callback=new_rpm)
connection.start()

# the callback will now be fired upon receipt of new values

time.sleep(60)
connection.stop()