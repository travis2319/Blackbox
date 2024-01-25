#include "TRIGGER_WIFI.h"               /*Includes ESP8266WiFi.h and WiFiClientSecure.h, just have these two libraries downloaded before*/
#include "TRIGGER_GOOGLESHEETS.h"       /*Library file for Google Sheets, has to be used after Wi-Fi Client Secure declaration, here everything is in Trigger_WIFI.h, so using it after Trigger_WIFI.h*/
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <ESP8266WiFi.h>

/**********Google Sheets Definations***********/
char column_name_in_sheets[ ] [10]= {"value1","value2","value3"};                        /*1. The Total no of column depends on how many value you have created in Script of Sheets;2. It has to be in order as per the rows decided in google sheets*/
String Sheets_GAS_ID = "AKfycbwKsjXy6wHFgOHF5Xlh1lSIE3bsig6YElwq0Z2I32lWKNe924_vjeIEjJb5409aSdM4oQ";                                         /*This is the Sheets GAS ID, you need to look for your sheets id*/
int No_of_Parameters = 3;                                                                /*Here No_of_Parameters decides how many parameters you want to send it to Google Sheets at once, change it according to your needs*/
/*********************************************/

SoftwareSerial SerialGPS(4, 5);

// #define gpsRxPin D1
// #define gpsTxPin D2
// SoftwareSerial SerialGPS(gpsRxPin,gpsTxPin);

TinyGPSPlus gps;

const char* ssid = "Travis";
const char* password = "Travis1915";

float Latitude , Longitude;
int year , month , date, hour , minute , second;
String DateString , TimeString , LatitudeString , LongitudeString;

void setup()
{

  SerialGPS.begin(9600);
  Serial.begin(9600);
  while (!Serial);

  WIFI_Connect("Pawsala","Travis1915");                                                     /*Provide you Wi-Fi SSID and password to connect to Wi-Fi*/
  Google_Sheets_Init(column_name_in_sheets, Sheets_GAS_ID, No_of_Parameters );         /*Sets the column name for Google Sheets, the GAS ID, and the No of Parameter we want to send*/
}

void loop()
{
  
   float a = 1, b = 2, c = 3;

   Data_to_Sheets(No_of_Parameters, a, b, c);         /*1. This function accepts multiple float parameter, here No_of_Parameters decides how many parameters you want to send to Google Sheets; 2. The values sent should be in order as per the column in Google Sheets*/

  Serial.println();
    delay(10000);                                       /*10 Sec Delay, Here 10 second delay is just used so that we can see the data pushed to sheets one by one
                                                        There is nothing like a minimum delay between two data push*/
}