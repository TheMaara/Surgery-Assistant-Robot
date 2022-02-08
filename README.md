# Surgery Assistant Robot

 A robot that helps surgeons make less mistakes during surgery by handling the surgical equipment instead of having human surgical assistants.

 The robot would have a camera whose visual input would be fed to the object detection algorithm. On recognising a tool the robots arm would move to pick up the tool and present it to the surgeon.

 Also when the surgeon is done with a particular tool he would present it to the robot and it would pick up the tool, rinse it and return it to the tool tray.
 
 ### This project was done by:
1. [Mark Maara](https://linkedin.com/in/mark-maara-42b235153/)
2. Samuel Muga.
3. Martin Juma.
4. Martin Kamau.
 
 ## Mechanical design.
 The Mechanical design is as shown below.
 
![robot](https://user-images.githubusercontent.com/68475422/150491125-58e32467-a1ec-4b1a-9e58-baf6bf318124.png)

 ## Surgical tools object detection AI.

 The object detection AI was made using Jupyter notebooks written by Nicholas Renotte.
 The notebooks are a detailed walkthrough on how to create an object detection system that can detect virtually anything.
 Github link to Renotte's Repository: https://github.com/nicknochnack/TFODCourse. It uses the SSD Mobilenet V2 FPNLite 320 by 320 pretrained model from the tensorflow model zoo because it is fast and not very resource heavy and so will be perfect for being deployed on a raspberry pi.
 A video demonstration of the functioning of the object detection algorithm is as shown below:
 
 [![oj](https://user-images.githubusercontent.com/68475422/150492996-be428e83-0fa1-42cd-a365-0c4db705bfd8.png)](https://youtu.be/K-EPAwUYiv4)


 ## Electrical and electronics module.
 The robot would use two cameras each tracking the arm that's on its respective side. The arms would be actuated by two stepper motors and three servo motors therefore giving it six axes of motion. All this would be run on a raspberry pi running the programs for the control of the motors and the object detection.
 
 ![Circuit](https://user-images.githubusercontent.com/68475422/150492569-01baf93a-651c-4444-832f-c87554d122c6.png)

  ## Robot model

 The robot model was designed and tested in autodesk inventor.
