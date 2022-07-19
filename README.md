# licence-plate-recognition

What is this:
  This code is part of a larger project. So please don't judge him right now. It does recognise license plates characters and return as a list.

The idea: 
  The idea after this project is an automated garrage door opener.

How it will be work:
  Raspberry pi with a camera search for license plates. When it finds a licence plate, raspi calls "python" gods to use "OCR" black magic and it reads the plate. After a quick check if the plate is correct. Pi calls Arduino to send a input to the relay so the actuator can open the garage gate automaticly

What stage am I at:
  I am currently code the licence plate recogniser in python, relay control code for arduino.
  
What will be coming next:
  License plate recognition in live feed from a camera (currently waiting rpi camera order to come). Some fine adjustment in arduino code so the relay work better in real life scenarios.
