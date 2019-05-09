from datetime import datetime 
from collections import deque 
from module import image 
from inout import camera_handler 

import RPi.GPIO as GPIO 
import time

class io_handler : 

    def __init__(self, **kwargs): 

        # Injected instance, apply rule [2]
        self.master_fifo = ''

        self.D_TX = 8
        self.D_RX = 10 
        self.P1 = 11
        self.P2 = 13
        self.AOS_SAT = 15
        self.CAMERA_CAPTURE = 12 
        self.PTT = 7
        
        self.datetime = kwargs['datetime']

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([self.P1, self.P2, self.CAMERA_CAPTURE], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        GPIO.setup([[self.PTT], GPIO.OUT, initial=GPIO.LOW)
        GPIO.add_event_detect(P1, GPIO.FALLING, self.handle) 
        GPIO.add_event_detect(P2, GPIO.BOTH, self.handle)         
        GPIO.add_event_detect(CAMERA_CAPTURE, GPIO.FALLING, self.handle) 

    # Inter-dependent class, apply rule [1]
    def set_master_fifo(self, master_fifo): 
        self.master_fifo = master_fifo
    
    # Rule [1] dependent instance, apply rule [3] 
    def set_camera_handler(self, **kwargs):
        self.camera_handler = camera_handler.camera_handler(
                    mode = kwargs['mode'],
                    datetime = self.datetime,
                    fifo = self.master_fifo
                )

    def handle(self, pin):
        if(pin == CAMERA_CAPTURE): 
            self.camera_handler.trigger()             
    
    def ptt_high(self):
        GPIO.output(self.PTT, GPIO.HIGH)

    def ptt_low(self):
        GPIO.output(self.PTT, GPIO.LOW)    

    def aos_out(self): 
        GPIO.output(self.AOS_SAT, GPIO.HIGH) 
