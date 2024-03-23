from bluepy.btle import Scanner, DefaultDelegate, Peripheral

# Define your device's MAC address
DEVICE_MAC_ADDRESS = 'f7:51:5e:4e:0d:32'

# Define the UUID of the GATT characteristic you want to read
CHARACTERISTIC_UUID = '00002a37-0000-1000-8000-00805f9b34fb'  # Replace XXXX with the actual UUID

class ScanDelegate(DefaultDelegate):
    def _init_(self):
        DefaultDelegate._init_(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print(f"Discovered device: {dev.addr}")

# Scan for the device
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

# Connect to the device
device = None
for dev in devices:
    if dev.addr == DEVICE_MAC_ADDRESS:
        device = Peripheral(dev)
        break

if device is None:
    print("Device not found.")
    exit()

# Get the service and characteristic
service = device.getServiceByUUID('00002a37-0000-1000-8000-00805f9b34fb')  # Replace XXXX with the service UUID
characteristic = service.getCharacteristics(CHARACTERISTIC_UUID)[0]

# Read the characteristic value
value = characteristic.read()

# Print the value
print("Value:", value)

# Disconnect from the device
device.disconnect()