from image import Image

class Taskrunner : 
    def __init__(self, callsign) : 
        self.callsign = callsign
        self.listtask = {
                "GETIMAGE" : capture, 
                "GETTELEMETRY" : null
            }


    def command(self, callsign, command) :
        if (callsign == self.callsign):
            
