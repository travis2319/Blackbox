#include <TinyGPS++.h>
#include <SoftwareSerial.h>
/* Create object named bt of the class SoftwareSerial */
SoftwareSerial GPS_SoftSerial(4, 5);/* (Rx, Tx) */
/* Create an object named gps of the class TinyGPSPlus */
TinyGPSPlus gps;              

void setup() {
 Serial.begin(9600);   /* Define baud rate for serial communication */
 GPS_SoftSerial.begin(9600); /* Define baud rate for software serial communication */
}

void loop() {
       smartDelay(1000);     /* Generate precise delay of 1ms */
        unsigned long start;
        double lat_val, lng_val, alt_m_val;
        uint8_t hr_val, min_val, sec_val;
        bool loc_valid, alt_valid, time_valid;
       lat_val = gps.location.lat();     /* Get latitude data */
       loc_valid = gps.location.isValid();     /* Check if valid location data is available */
       lng_val = gps.location.lng();     /* Get longtitude data */
       alt_m_val = gps.altitude.meters();      /* Get altitude data in meters */
        alt_valid = gps.altitude.isValid();     /* Check if valid altitude data is available */
       hr_val = gps.time.hour() + 5;   /* Get hour */
       min_val = gps.time.minute() + 30;      /* Get minutes */
       sec_val = gps.time.second();      /* Get seconds */
       time_valid = gps.time.isValid();  /* Check if valid time data is available */
        if (!loc_valid)
       {         
         Serial.print("Latitude : ");
         Serial.println("*****");
         Serial.print("Longitude : ");
         Serial.println("*****");
        }
        else
        { 
         Serial.print("Latitude : "); /* printing Latitude*/
         Serial.println(lat_val, 6);
          
         Serial.print("Longitude : "); /* printing Longitude*/
         Serial.println(lng_val, 6);
        }
        
        if (!alt_valid)
        {
         Serial.print("Altitude : ");
         Serial.println("*****");
        }
        else
        {
         Serial.print("Altitude : ");
         Serial.println(alt_m_val, 6);   
        }

        if (!time_valid)
        {
         Serial.print("Time : ");
         Serial.println("*****");
        }
        else
        { 
          if(hr_val > 12){
            hr_val = hr_val - 12;
          }
          if(min_val > 60){
          hr_val  = hr_val + 1;
          min_val = min_val - 60;
          }
         char time_string[32];
         sprintf(time_string, "Time : %02d:%02d:%02d \n", hr_val, min_val, sec_val);
         Serial.print(time_string);   
        }
}

static void smartDelay(unsigned long ms)
{
  unsigned long start = millis();
  do 
  {
    while (GPS_SoftSerial.available())    /* Encode data read from GPS while data is available on serial port */
     gps.encode(GPS_SoftSerial.read());
/* Encode basically is used to parse the string received by the GPS and to store it in a buffer so that information can be extracted from it */
  } while (millis() - start < ms);
}
