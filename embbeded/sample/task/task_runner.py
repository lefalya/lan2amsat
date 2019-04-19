from module import image
from module import tle 

sstv_mode = "Robot36"

class task_runner : 
    def __init__(self, **kwargs) : 
        self.callsign = kwargs["callsign"]
        self.main = kwargs["main"]
        self.master_fifo = kwargs['fifo']
        self.tle = tle()
        self.image = image(
                mode = kwargs['mode'],
                datetime = kwargs['datetime'])

    def parse_command(self, callsign, message) :
        if callsign == self.callsign :
            self.execute(message)
            
    def execute(self, command):
        if "#" not in command :
            self.single_command(command)
        else: 
            self.command_with_message(command)

    def single_command(self, command):
        if command == "CAPTURE" :
            self.image.capture()
        elif command == "LOOPBACK": 
            print("LOOPBCK")

    def command_with_message(self, buff):
        buff = buff.split('#') 
        command = buff[0]
        message = buff[1]

        if command == "TLE":
            self.main.calculate_az_el = False 
            self.tle.set_tle(message)
            self.main.calculate_az_el = True 
            
