from datetime import datetime 
from collections import deque 
from module import image 
from inout import camera_handler 

import RPi.GPIO as GPIO 
import time

D_TX = 8
D_RX = 10 
P1 = 11
P2 = 13
AOS_SAT = 15
CAMERA_CAPTURE = 12 

class io_handler : 

    def __init__(self, **kwargs): 
        self.master_fifo = kwargs['fifo']
        self.camera_handler = camera_handler.camera_handler(self.master_fifo)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([P1, P2, CAMERA_CAPTURE], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        #GPIO.setup([AOS_SAT], GPIO.OUT, initial=GPIO.HIGH)
        GPIO.add_event_detect(P1, GPIO.FALLING, self.handle) 
        GPIO.add_event_detect(P2, GPIO.BOTH, self.handle)         
        GPIO.add_event_detect(CAMERA_CAPTURE, GPIO.FALLING, self.handle) 

    def handle(self, pin):
        if(pin == CAMERA_CAPTURE): 
            self.camera_handler.trigger()             

    def aos_out(self): 
        GPIO.output(AOS_SAT, GPIO.HIGH) 
