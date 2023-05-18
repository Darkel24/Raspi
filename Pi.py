EXP 8:
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
coil_A1_pin = 22
coil_A2_pin = 24
coil_B1_pin = 26
coil_B2_pin = 28
GPIO.setup(coil_A1_pin, GPIO.OUT)
GPIO.setup(coil_A2_pin, GPIO.OUT)
GPIO.setup(coil_B1_pin, GPIO.OUT)
GPIO.setup(coil_B2_pin, GPIO.OUT)
forward = ['1010', '0110', '0101', '1001']
backward = ['1001', '0101', '0110', '1010']
def forw(delay, steps):
    for i in range(steps):
        for step in forward:
            print(step)
            set_step(step)
            time.sleep(delay)
def back(delay, steps):
    for i in range(steps):
        for step in backward:
            print(step)
            set_step(step)
            time.sleep(delay)
def set_step(step):
    GPIO.output(coil_A1_pin, step[0] == '1')
    GPIO.output(coil_A2_pin, step[1] == '1')
    GPIO.output(coil_B1_pin, step[2] == '1')
    GPIO.output(coil_B2_pin, step[3] == '1')
while(True):
    choice = input("Enter your choice - Forward [F/f] -Backward [B/b] - Stop [S/s]: ")
    if(choice == 'F' or choice == 'f'):
        print("Forward Motion")
        set_step('0000')
        forw(1,2)
        set_step('0000')
        time.sleep(2)
    if(choice == 'B' or choice == 'b'):
        print("Backward Motion")
        set_step('0000')
        back(1,2)
        set_step('0000')
        time.sleep(2)
    if(choice == 'S' or choice == 's'):
        print("STOP!!!")
        break
EXP 9:
from gpiozero import LED,Button
led1=LED(17)
led2=LED(18)
button=Button(2)
led2.on()
while(True):
    button.wait_for_press()
    print("BUTTON PRESSED!!")
    led1.on()
    led2.off()
    button.wait_for_release()
    print("BUTTON RELEASED!!")
    led1.off()
    led2.on()
EXP 10 :
1. To write a python program to display(scrolling) “RASPBERRY PI ” in sensehat LED matrix display and execute it in the Sense HAT simulator

from sense_hat import SenseHat
import time

sense = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)

message = "RASPBERRY PI"

speed = 1
text_color = green

while True:
    sense.show_message(message, speed, text_color)

2. To write a python program to display “give way” traffic symbol and diode symbol and execute it in the Sense HAT simulator

from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
def space():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
def diode():
    P = pink
    O = nothing
    logo = [
    O, O, O, P, P, O, O, O,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, P, O, O, P, O, O,
    O, P, O, O, O, O, P, O,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    ]
    return logo
def giveway():
    P = pink
    O = nothing
    logo = [
    P, P, P, O, O, O, O, O,
    P, P, P, P, O, O, O, O,
    P, P, O, P, P, O, O, O,
    P, P, O, O, P, P, O, O,
    P, P, O, O, P, P, P, O,
    P, P, O, P, P, P, O, O,
    P, P, P, P, O, O, O, O,
    P, P, P, O, O, O, O, O,
    ]
    return logo
images = [diode, space, giveway, space]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1

POST LAB QUESTIONS
1. Write the statements to display in red clour and orange clour in Sense HAT  matrix display
RED

from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
def r():
    R = red
    logo = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    ]
    return logo
images = [r]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1

BLUE

from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
blue = (0, 0, 255)
def b():
    B = blue
    logo = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return logo
images = [b]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1

2. Give the python code to display Nike symbol in blue color

from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
blue = (0, 0, 255)
white = (255,255,255)
def b():
    B = blue
    O = white
    logo = [
    B, B, B, O, O, O, O, O,
    O, B, B, B, O, O, O, O,
    O, O, B, B, B, O, O, O,
    O, O, O, B, B, B, O, O,
    O, O, O, O, B, B, B, O,
    O, O, O, O, O, B, B, B,
    O, O, O, O, B, B, B, O,
    O, O, O, B, B, B, O, O,
    ]
    return logo
images = [b]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
EXP 11
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
while True:
    input_state=GPIO.input(21)
    if input_state==True:
        print("Motion Detected")
    else:
        print("none")
        time.sleep(0.05)
EXP 12
from bottle import route,run,request 
tempr=input("enter the temperature value:") 
hum=input("enter the humidity:") 
ws=input("enter the windspeed:") 
rain=input("enter rainy or not:")
@route('/')
def getsens(): 
    sensor_log=[{'sensor':'Temperature','value':tempr},
    {'sensor':'humidity','value':hum},
    {'sensor':'wind speed','value':ws},
    {'sensor':'rain','value':rain}]
    return dict(data=sensor_log)
run(host='localhost',port=7000,debug=True)

EXP 13 :
from time import sleep
import paho.mqtt.client as mqtt 
import json

host = 'demo.thingsboard.io' 
access_token = 'd8iPsPtMZMkqD5eyW7W4'
sensor_data = {'temperature':0,'humidity':0,'windspeed':0,'rain sensor':'not rainy'} 
client = mqtt.Client()
client.username_pw_set(access_token)

while True:
    sensor_data['temperature'] = 70
    sensor_data['humidity'] = 40
    sensor_data['windspeed'] = 50 
    sensor_data['rain sensor'] = 'not rainy' 
    client.connect(host, 1883, 20)
    client.publish('v/devices/me/telemetry',json.dumps(sensor_data),1) 
    client.disconnect()
    sleep(10)  
