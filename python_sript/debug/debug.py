import obd

ports=obd.scan_serial()
print(ports)