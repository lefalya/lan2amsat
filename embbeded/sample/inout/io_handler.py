from collections import deque 
from module import image 
from inout import camera_handler 
from inout import serial_handler

import RPi.GPIO as GPIO 
import time
import serial 

class io_handler : 

    def __init__(self, **kwargs): 

        # Injected instance, apply rule [2]
        self.master_fifo = ''
        self.sh = ''
        self.ser = ''

        try :
            self.ser = serial.Serial('/dev/ttyACM0',
                    9600,
                    timeout=0) 
        except : 
            print('Running Without Serial Host')

        self.D_TX = 8
        self.D_RX = 10 
        self.P1 = 11
        self.P2 = 13
        self.AOS_SAT = 15
        self.CAMERA_CAPTURE = 7 
        self.PTT = 12
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([self.P1, self.P2, self.CAMERA_CAPTURE], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        GPIO.setup([self.PTT], GPIO.OUT, initial=GPIO.LOW)
        GPIO.add_event_detect(self.P1, GPIO.FALLING, self.handle) 
        GPIO.add_event_detect(self.P2, GPIO.BOTH, self.handle)         
        GPIO.add_event_detect(self.CAMERA_CAPTURE, GPIO.FALLING, self.handle) 

    # Inter-dependent class, apply rule [1]
    def set_master_fifo(self, master_fifo): 
        self.master_fifo = master_fifo
    
    # Rule [1] dependent instance, apply rule [3] 
    def set_serial_handler(self): 
        self.sh = serial_handler.serial_handler(
                master_fifo = self.master_fifo, 
                master_io=self)
        
    # Rule [1] dependent instance, apply rule [3] 
    def set_camera_handler(self, **kwargs):
        self.camera_handler = camera_handler.camera_handler(
                    mode = kwargs['mode'],
                    fifo = self.master_fifo
                )

    def read_serial(self):
        if self.ser != '' :
            data = self.ser.read(300) 
            self.sh.parse(data) 
        else : 
            data = '' 

    def write_serial(self, data): 
        self.ser.write(bytes(data, 'utf-8')) 

    def handle(self, pin):
        if(pin == self.CAMERA_CAPTURE): 
            print('PIN ACTIVATED')
#            self.camera_handler.trigger()             
    
    def ptt_high(self):
        GPIO.output(self.PTT, GPIO.HIGH)

    def ptt_low(self):
        GPIO.output(self.PTT, GPIO.LOW)    

    def aos_out(self): 
        GPIO.output(self.AOS_SAT, GPIO.HIGH) 
