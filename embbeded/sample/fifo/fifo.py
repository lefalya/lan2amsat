from collections import deque 
from fifo import picture_data 

class fifo: 
    
    def __init__(self): 
        self.fifo = deque() 

    def append(self, data): 
        self.fifo.append(data)

    def get_fifo_list(self): 
        print(self.fifo)

    # construct picture fifo object 
    def construct_picture(self, **kwargs): 
        pc = picture_data.picture_data() 
        pc.set_path(kwargs["path"]) 
        pc.set_alt(kwargs["alt"]) 
        self.append(pc) 

