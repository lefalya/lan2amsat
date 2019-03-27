import RPi.GPIO as GPIO 

D_TX = 8
D_RX = 10 
P1 = 11
P2 = 13
AOS_SAT = 15
CAMERA_CAPTURE = 12 

class pinHandler : 

    def __init__(): 
        GPIO.setup([P1, P2, CAMERA_CAPTURE], GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
        GPIO.setup([AOS_SAT], GPIO.OUT, initial=GPIO.HIGH)
        GPIO.add_event_detect(P1, GPIO.BOTH, self.handle) 
        GPIO.add_event_detect(P2, GPIO.BOTH, self.handle)         
        GPIO.add_event_detect(CAMERA_CAPTURE, GPIO.RISING, self.handle) 
    
    def handle(pin): 
        print(pin)

    def aos_out(): 
        GPIO.output(AOS_SAT, GPIO.HIGH) 
