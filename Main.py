import RPi.GPIO as GPIO
from SimpleCV import Image, Display
from time import sleep as sleep

display = Display()
img = Image("School.jpg")

state = 1
speed = 50

Motor_1 = 4
Motor_2 = 17

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_1, GPIO.OUT)

pwm = GPIO.PWM(Motor_1, 500)

def worker():
       if(state = 3):
              global state = 1
       else:
              global state = state + 1
       if(state = 1):
              global speed = 50
       elif(state = 2):
              global speed = 70
       elif(state = 3):
              global speed = 90
       GPIO.output(Motor_1, True)
       GPIO.output(Motor_2, False)
       pwm.changeDutyCycle(speed)
       monitor(state)
       sleep(120)

def monitor(): 
        
while True:
       cmd = raw_input("Command:")
        if(cmd[0] = "s"):
                GPIO.cleanup()
                exit()
       worker()

       
