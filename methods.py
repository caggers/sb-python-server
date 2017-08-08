"""
An entire file for you to expand. Add methods here, and the client should be
able to call them with json-rpc without any editing to the pipeline.
"""
from nanpy import (Servo, ArduinoApi, SerialManager)
from time import sleep



lightsPin = 7
ledState = False

servo = Servo(9)
servo.write(0)

tempPin = 6

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")
    
a.pinMode(lightsPin, a.OUTPUT)
a.pinMode(tempPin, a.OUTPUT)


def toggle_led(on):
    if on:
        a.digitalWrite(lightsPin, a.HIGH)
    else:
        a.digitalWrite(lightsPin, a.LOW)
        
def move_servo(val):
    servo.write(val)

def change_temp(val):
    a.analogWrite(tempPin, val)
	
	
	
	
