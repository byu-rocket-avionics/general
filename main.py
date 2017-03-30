import RPi.GPIO as GPIO
import time
from time import sleep

# This is a script to be used on the Raspberry Pi
# in the ignition box and will be activated via 
# an ssh command.  

CONNECTION_LED = 27
IGNITE = 14 
DONE_LED = 22
progEnd = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(CONNECTION_LED,GPIO.OUT) # CONNECTION LED on pin 27
GPIO.setup(IGNITE,GPIO.OUT) # IGNITION on pin 14
GPIO.setup(DONE_LED,GPIO.OUT) # DONE on pin 22

GPIO.output(CONNECTION_LED,GPIO.HIGH)

print('\n********************\n\n')
print('AIAA BYURPG Ignition Program')
print('created Feb 11, 2017\n\n')
print('********************')

while progEnd == False:

  print('\n\nMain Menu\n')
  print('   1. Arm Motor')
  print('   2. Checklist')
  print('   3. Restart')
  print('   4. Exit\n')
  c = raw_input('choice: ')

  if c == "1":
    p = raw_input('\nPassword: ')
    if p == "kevincanfly":
       ign = raw_input('\nIGNITE (yes/no): ')
       if ign == "y" or ign == "Y" or ign == "yes":
          
          print "\nIGNITE on"
          GPIO.output(IGNITE,GPIO.HIGH)
          time.sleep(5)
          print "IGNITE off\n"
          GPIO.output(IGNITE,GPIO.LOW)
          GPIO.output(DONE_LED,GPIO.HIGH)

       else:
          print "Ignition avoided"
    else:
        print "Error: Invalid Password"

  elif c == "2":
     print "Checklist"
  elif c == "3":
     print "\nRESTARTING\n"
     GPIO.output(DONE_LED,GPIO.LOW)
  elif c == "4":
     print "Ending Program"
     progEnd = True
     GPIO.output(DONE_LED,GPIO.LOW)
     GPIO.output(CONNECTION_LED,GPIO.LOW)
  else:
     print "Invalid Input" 

