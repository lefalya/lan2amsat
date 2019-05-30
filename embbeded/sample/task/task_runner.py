from module import image
from module import tle 

sstv_mode = "Robot36"

class task_runner : 
    def __init__(self, **kwargs) : 
        self.callsign = kwargs["callsign"]
        self.main = kwargs["main"]
        self.master_fifo = kwargs['fifo'] # rule [2]
        self.master_io = kwargs['io']
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

        if command == "LOOPBACK":
            live_response = '200'
            self.master_fifo.construct_message(
                    message=live_response,
                    live=True)
            
        # live image capture 
        if command == "CAPTURE" :
            live_response = '201'
            self.master_fifo.construct_message(
                    message=live_response,
                    live=True)

            path, datetime = self.image.capture()
            self.master_fifo.construct_picture(
                    path=path, 
                    datetime=datetime,
                    alt=datetime,
                    live=True) 

        # get fifo content 
        elif command == "GETFIFOCONTENT": 
            self.master_fifo.get_fifo_list() 

        # pop all fifo's element
        elif command == "POPALLFIFO":
            self.master_fifo.pop_all()

    def command_with_message(self, buff):
        buff = buff.split('#') 
        command = buff[0]
        message = buff[1]

        if command == "TLE":
            self.main.calculate_az_el = False 
            self.tle.set_tle(message)
            self.main.calculate_az_el = True 

        if com == 'PAS':
           self.io.write_serial(message) 
