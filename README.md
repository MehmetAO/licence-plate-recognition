# licence-plate-recognition

### The idea
The idea after this project is an automated garrage gate.

### What it does
When you came in front of your garage, it recognise your car from your licence plate and open the gate automatically

### How it works
A camera attached to Raspberry pi processing video real time and looking for license plates. When it find a licese plate, turn that image to characters and compare it with my plate. If the comparison turns "True" it sends a serial input to Arduino which turns the relay on and active the actuator. Finally the actuator runs and open the gate for me.

### What Stage am I at
I am currently optimising for continues video feed
