from obd import OBDStatus

 
 # status= OBDStatus.NOT_CONNECTED
 # print(status)

 if OBDStatus.NOT_CONNECTED != NULL:
    print(OBDStatus.NOT_CONNECTED)
 elif OBDStatus.ELM_CONNECTED != NULL:
    print(OBDStatus.ELM_CONNECTED)
 elif OBDStatus.OBD_CONNECTED != NULL:
    print(OBDStatus.OBD_CONNECTED)
 elif OBDStatus.CAR_CONNECTED != NULL:
    print(OBDStatus.CAR_CONNECTED)
 else  print("code error")