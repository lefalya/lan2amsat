import RPi.GPIO as GPIO 
import time
from datetime import datetime 
from collections import deque 
from module import image 

D_TX = 8
D_RX = 10 
P1 = 11
P2 = 13
AOS_SAT = 15
CAMERA_CAPTURE = 12 

class io_handler : 

    def __init__(self, **kwargs): 
        #interval queue
        self.qint = deque(maxlen=2)
        self.camera_thold = False 
        self.camera_int_time = '' 
        self.master_fifo = kwargs['fifo'] 

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([P1, P2, CAMERA_CAPTURE], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        #GPIO.setup([AOS_SAT], GPIO.OUT, initial=GPIO.HIGH)
        GPIO.add_event_detect(P1, GPIO.FALLING, self.handle) 
        GPIO.add_event_detect(P2, GPIO.BOTH, self.handle)         
        GPIO.add_event_detect(CAMERA_CAPTURE, GPIO.FALLING, self.handle) 

    def handle(self, pin):
        print("interrupt from : ", pin) 

        if(pin == CAMERA_CAPTURE): 
            path, time = image.capture() 
            self.master_fifo.construct_picture(
                    path = "/picture",
                    alt = "new picture"
                )
            
        '''
        dt = datetime.utcnow() 
        self.qint.append(dt)  
        if(len(self.qint) ==2):
            interval = (self.qint[1]-self.qint[0]).total_seconds()
            print(self.qint[1]," - ",self.qint[0]," = ",interval)
        '''

    def aos_out(self): 
        GPIO.output(AOS_SAT, GPIO.HIGH) 
'''
if __name__ == "__main__" : 
    io = io_handler()
    while True : 
        time.sleep(1e6) 
'''
