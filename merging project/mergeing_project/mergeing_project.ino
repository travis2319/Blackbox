#include "TRIGGER_WIFI.h"               /*Includes ESP8266WiFi.h and WiFiClientSecure.h, just have these two libraries downloaded before*/
#include "TRIGGER_GOOGLESHEETS.h"       /*Library file for Google Sheets, has to be used after Wi-Fi Client Secure declaration, here everything is in Trigger_WIFI.h, so using it after Trigger_WIFI.h*/
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

/**********Google Sheets Definations***********/
char column_name_in_sheets[ ] [10]= {"value1","value2","value3"};                        /*1. The Total no of column depends on how many value you have created in Script of Sheets;2. It has to be in order as per the rows decided in google sheets*/
String Sheets_GAS_ID = "AKfycbwKsjXy6wHFgOHF5Xlh1lSIE3bsig6YElwq0Z2I32lWKNe924_vjeIEjJb5409aSdM4oQ";                                         /*This is the Sheets GAS ID, you need to look for your sheets id*/
int No_of_Parameters = 3;                                                                /*Here No_of_Parameters decides how many parameters you want to send it to Google Sheets at once, change it according to your needs*/
/*********************************************/

/* Create object named bt of the class SoftwareSerial */
SoftwareSerial SerialGPS(4, 5);/* (Rx, Tx) */
/* Create an object named gps of the class TinyGPSPlus */
TinyGPSPlus gps;              

const char* ssid = "Travis";
const char* password = "Travis1915";

void setup() {
 Serial.begin(9600);   /* Define baud rate for serial communication */
 SerialGPS.begin(9600); /* Define baud rate for software serial communication */

 WIFI_Connect("Pawsala","Travis1915");                                                     /*Provide you Wi-Fi SSID and password to connect to Wi-Fi*/
  Google_Sheets_Init(column_name_in_sheets, Sheets_GAS_ID, No_of_Parameters );         /*Sets the column name for Google Sheets, the GAS ID, and the No of Parameter we want to send*/
}

void loop() {
       smartDelay(1000);     /* Generate precise delay of 1ms */
        unsigned long start;
        double lat_val, lng_val, alt_m_val;
        uint8_t hr_val, min_val, sec_val;
        bool loc_valid, alt_valid, time_valid;
        float a , b, c;
       lat_val = gps.location.lat();     /* Get latitude data */
       loc_valid = gps.location.isValid();     /* Check if valid location data is available */
       lng_val = gps.location.lng();     /* Get longtitude data */
       alt_m_val = gps.altitude.meters();      /* Get altitude data in meters */
        alt_valid = gps.altitude.isValid();     /* Check if valid altitude data is available */
       hr_val = gps.time.hour() + 5;   /* Get hour */
       min_val = gps.time.minute() + 30;      /* Get minutes */
       sec_val = gps.time.second();      /* Get seconds */
       time_valid = gps.time.isValid();  /* Check if valid time data is available */
        if (!loc_valid && !alt_valid )
       {         
         Serial.print("Latitude : ");
         Serial.println("*****");
         Serial.print("Longitude : ");
         Serial.println("*****");
         Serial.print("Altitude : ");
         Serial.println("*****");
        }
        else
        { 
         Serial.print("Latitude : "); /* printing Latitude*/
         Serial.println(lat_val, 6);
          
         Serial.print("Longitude : "); /* printing Longitude*/
         Serial.println(lng_val, 6);

         Serial.print("Altitude : "); /* printing Longitude*/
         Serial.println(alt_m_val, 6);
          a = lat_val, b = lng_val,c=alt_m_val; 
          Data_to_Sheets(No_of_Parameters, a, b, c);         /*1. This function accepts multiple float parameter, here No_of_Parameters decides how many parameters you want to send to Google Sheets; 2. The values sent should be in order as per the column in Google Sheets*/
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
    while (SerialGPS.available())    /* Encode data read from GPS while data is available on serial port */
     gps.encode(SerialGPS.read());
/* Encode basically is used to parse the string received by the GPS and to store it in a buffer so that information can be extracted from it */
  } while (millis() - start < ms);
}
