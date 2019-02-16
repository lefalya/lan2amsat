from module import image
from fifo import picture_fifo 

sstv_mode = "Robot36"

class task_runner : 
    def __init__(self, callsign) : 
        self.callsign = callsign
        self.picture_fifo = picture_fifo()
        self.image = image(sstv_mode, self.pictures)

    def parse_command(self, callsign, message) :
        print(callsign)
        print(message)
        print(callsign==self.callsign)
        if callsign == self.callsign :
            self.execute(message)
            
    def execute(self, message):
        if message == "CAPTURE" : 
            self.image.capture()
