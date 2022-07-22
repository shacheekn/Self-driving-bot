import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BCM)
from gpiozero import DistanceSensor
GPIO.setwarnings(False)
sensor1= DistanceSensor(echo=24,trigger=23)
class Motor():
    def _init_(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA,GPIO.OUT)
        GPIO.setup(self.In1A,GPIO.OUT)
        GPIO.setup(self.In2A,GPIO.OUT)
        GPIO.setup(self.EnaB,GPIO.OUT)
        GPIO.setup(self.In1B,GPIO.OUT)
        GPIO.setup(self.In2B,GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA, 100);
        self.pwmA.start(0);
        self.pwmB = GPIO.PWM(self.EnaB, 100);
        self.pwmB.start(0);

    def move(self,speed=1,turn=0,t=0):
        speed *=100
        turn *=100
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        if leftSpeed>100: leftSpeed=100
        elif leftSpeed<-100: leftSpeed= -100
        if rightSpeed>100: rightSpeed=100
        elif rightSpeed<-100: rightSpeed= -100

        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        if leftSpeed>0:
            GPIO.output(self.In1A,GPIO.HIGH)
            GPIO.output(self.In2A,GPIO.LOW)
        else:
            GPIO.output(self.In1A,GPIO.LOW)
            GPIO.output(self.In2A,GPIO.HIGH)

        if rightSpeed>0:
            GPIO.output(self.In1B,GPIO.HIGH)
            GPIO.output(self.In2B,GPIO.LOW)
        else:
            GPIO.output(self.In1B,GPIO.LOW)
            GPIO.output(self.In2B,GPIO.HIGH)

        sleep(t)
    def stop(self,t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        sleep(t)


def main():
    distance=sensor1.distance*100
    print(distance)
    if distance<15:
        motor.stop(2)
        time.sleep(0.1)

    else:
        motor.move(-0.4,0,2)
        time.sleep(0.1)


if _name_ == '_main_':
    motor= Motor(25,22,27,26,6,5)
    while True:
        main()