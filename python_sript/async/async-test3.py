import obd
import csv


filename = "obd_data.csv"  # Define your desired filename
fieldnames = ["Timestamp", "RPM", "Speed"]  # Define CSV header names

# connection = obd.OBD("/dev/ttyACM0")
connection = obd.Async()
connection.watch(obd.commands.RPM)
connection.watch(obd.commands.SPEED)
connection.start()


with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        rpm = connection.query(obd.commands.RPM)
        speed = connection.query(obd.commands.SPEED)
        timestamp = str(datetime.datetime.now())  # Get current timestamp

        # Write data to CSV
        writer.writerow({"Timestamp": timestamp, "RPM": rpm, "Speed": speed})

        # Adjust delay between readings as needed
        time.sleep(1)
