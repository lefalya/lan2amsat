class Tracker_handler : 

    def __init__(self, master_io): 
        self.master_io = master_io 

    def parse_az_el(self, az, el): 
        az = round(float(az.split()[0])) 
        el = round(float(el.split()[0]))
        com = 'W'+self.to_string(az)+' '+self.to_string(el)
#        self.master_io.command_tracker(com)

    def to_string(self, num):
        numStr = str(num) 
        if num < 10:
            numStr = '00'+numStr
        elif num < 100: 
            numStr = '0'+numStr 
        
        return numStr

