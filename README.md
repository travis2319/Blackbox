In this study, we present two distinct models designed to enhance vehicle telemetry, thereby ensuring safety, compliance, and user accessibility. The first model prioritizes universal compatibility, while the second emphasizes user convenience and operational efficiency. Both models leverage advanced sensor technologies and data transmission protocols to collect and relay critical information to relevant authorities and users. The following journal entry provides a comprehensive overview of the working principles and functionalities of these two models.

Introduction: With the increasing emphasis on road safety and regulatory compliance, the integration of advanced telemetry systems in vehicles has become imperative. These systems not only facilitate real-time monitoring of vehicle performance and location but also enable seamless communication with regulatory bodies and users. In this context, we present two distinct telemetry models, each tailored to address specific operational requirements and user preferences.

Model 1: Universal Compatibility and Regulatory Compliance The first model is engineered to ensure universal compatibility with a wide range of vehicles, emphasizing seamless integration and regulatory compliance. Upon the initiation of the vehicle, the telemetry device, powered by an Arduino module, commences data collection from a suite of sensors, including piezoceramic (accelerometer), angular rate (gyro), Wi-Fi, GSM, NavIC GAGAN GPS receiver, RFID, and IR modules. Subsequently, the collected data is transmitted at regular intervals via the GSM module to the Regional Transport Office (RTO) services. Upon the cessation of vehicle operation, the system enters a dormant state, ensuring efficient power management.


![image](https://github.com/travis2319/Blackbox/assets/95576296/878af2b7-31d8-4882-ba02-6c5e49b1bf59)

Model 2: User-Centric Accessibility and Operational Efficiency In contrast, the second model prioritizes user accessibility, operational efficiency, and cost-effectiveness. Upon vehicle activation, the telemetry module synchronizes with the vehicle's systems and prompts the user to engage with a dedicated mobile application. The user is required to authenticate using biometric credentials and grant necessary permissions for location tracking, hotspot activation, and nearby device sharing. As the vehicle operates, the Arduino module interfaces with the vehicle's ECU sensors via the OBDII port, collecting real-time data and location information through the Wi-Fi module. Subsequently, the collected data is transmitted directly to the user's mobile application, with automatic backup and encryption for secure transmission to the RTO office and company servers at predefined intervals.


Conclusion: In conclusion, the comparative analysis of the two telemetry models underscores their distinct operational paradigms, catering to diverse stakeholder requirements. While the first model prioritizes universal compatibility and regulatory compliance, the second model emphasizes user-centric accessibility and operational efficiency. Both models represent significant advancements in vehicle telemetry, offering enhanced safety, regulatory compliance, and user convenience. Future research endeavors will focus on integrating the strengths of these models to develop a comprehensive telemetry solution that addresses the multifaceted needs of modern vehicular operations.


Verification and Testing of NEO 6m (GPS)
Over the past few months, our team has been focused on verifying and testing the functionality of the NEO 6m (GPS). We have successfully obtained output data, which we have integrated with a Google AppScript server (Web app). This data is now being stored and accessed using Google Excel sheets.

![image](https://github.com/travis2319/Blackbox/assets/95576296/9d7d6117-91ef-4c2a-a43a-2fe55233a4e6)



Step 1: Development of Transaction Process (MODEL 3)
Currently, our primary focus is on developing the transaction process. In this stage, we are implementing a stationary camera system (referred to as MODEL 3) to capture images of car number plates. These images will undergo an image recognition operation to decipher the numbers on the number plates.

Step 2: Cross-Checking with RTO Database and Contact Details Retrieval
Once the numbers on the number plates are deciphered, we will cross-check this information with the Regional Transport Office (RTO) database, which is freely available on the internet. This will allow us to retrieve the contact details of the vehicle owner.

Step 3: Bank Database Cross-Checking and Fund Deduction
Using the owner's contact details, we will then cross-check with the bank database to identify the account holder. Upon confirmation, we will deduct the specified amount from the owner's account and transfer it to a private business account. This process will be carried out separately from the deduction of funds from the owner's account via the bank.

These steps represent our current progress and focus in our ongoing project.
