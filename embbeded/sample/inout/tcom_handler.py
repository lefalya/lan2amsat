from module import image
from module import tle 

sstv_mode = "Robot36"

class tcom_handler : 
    def __init__(self, **kwargs) : 
        self.callsign = kwargs["callsign"]
        self.main = kwargs["main"]
        self.master_fifo = kwargs['fifo'] # rule [2]
        self.master_io = kwargs['io']
        self.tle = tle()
        self.image = image(mode = kwargs['mode'])
        self.delimiter = "@@@"

    def parse_command(self, callsign, message) :
        if callsign == self.callsign :
            self.execute(message)

    def execute(self, command):

        # @@@ is delimiter for command with message
        if self.delimiter not in command :
            self.single_command(command)
        else: 
            self.command_with_message(command)

    def single_command(self, command):

        if command == "LOOPBACK":
            live_response = 'LOOPBACK'
            self.master_fifo.construct_message(
                    message=live_response,
                    live=True)
            
        # live image capture 
        if command == "CAPTURE" :
            live_response = 'CAPTURE'
            self.master_fifo.construct_message(
                    message="CAPTURING",
                    live=True)

            path, datetime = self.image.capture()
            self.master_fifo.construct_picture(
                    path=path, 
                    datetime=datetime,
                    alt=datetime,
                    live=True) 
            
            self.master_fifo.construct_message(
                    message="CAPTUREDONE",
                    live=True)

        # get fifo content 
        elif command == "GETFIFOCONTENT": 
            epoch = self.master_fifo.get_fifo_list() 

        # pop all fifo's element
        elif command == "POPALLFIFO":
            self.master_fifo.pop_all()
        
        # get module's TLE epoch
        elif command == "GETEPOCH":
            epoch = self.main.tracker.get_epoch()
            self.main.fifo.construct_message(
                    message="MODEPOCH@@@"+epoch,
                    live=True)

    def command_with_message(self, buff):
        buff = buff.split(self.delimiter) 
        command = buff[0]
        message = buff[1]

        if command == "TLE":
            self.main.calculate_az_el = False 

            self.main.fifo.construct_message(
                    message="TLERECEIVED",
                    live=True)

            self.tle.set_tle(message)
            
            self.main.fifo.construct_message(
                    message="TLEDONE",
                    live=True)

            self.main.calculate_az_el = True 

        if command == 'PAS':
            print(message)
            self.master_io.write_serial(message) 
