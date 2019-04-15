from collections import deque 
from model import picture_data 
from module import encoder 
import os 

class fifo: 
    
    def __init__(self, callsign): 
        self.fifo = deque() 
        self.encoder = encoder(callsign)

    def append(self, data): 
        buff_path = self.encoder.generate_buff(data)
        data.set_buff_path(buff_path)
        self.fifo.append(data)

    def pop(self): 
        data = self.fifo.popleft() 
        bfpth = data.get_buff_path()
        self.encoder.play_buff(bfpth)

        if(data.get_type() == 'img') :
            os.system('rm '+data.get_path())

        os.system('rm '+bfpth) 

    def get_fifo(self): 
        return self.fifo

    def get_fifo_list(self): 
        print(self.fifo)

    # construct picture fifo object 
    def construct_picture(self, **kwargs): 
        pc = picture_data() 
        pc.set_path(kwargs["path"]) 
        pc.set_alt(kwargs["alt"]) 
        self.append(pc)
