import RPi.GPIO as GPIO
from time import sleep as sleep

state = 1
speed = 50

Motor_1 = 4
Motor_2 = 17

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_1, GPIO.OUT)

def set(property, val):
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(val)
        f.close()

set("deleyed, 0")
set("mode, pwm")
set("active, 1")
set("frequency, 500")

def worker:
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
       set("duty", str(speed))
       #monitor(state)
       sleep(120)
       
#def monitor:
while True:
       worker()
       
