from collections import deque 
from model import picture_data
from model import text_data 
from module import encoder 
import os 

class fifo: 
    
    def __init__(self, **kwargs): 
        self.fifo = deque()
        self.variables = kwargs['variables']
        self.date_time = kwargs['datetime']
        self.encoder = encoder(callsign = kwargs['callsign'],
                               variables = self.variables)

    def append(self, data): 
        buff_path = self.encoder.generate_buff(data)
        data.set_buff_path(buff_path)
        self.fifo.append(data)

    def append_left(self,data): 
        buff_path = self.encoder.generate_buff(data) 
        data.set_buff_path(buff_path) 
        self.fifo.appendleft(data)

    def pop(self):
        try :
            data = self.fifo.popleft() 
            bfpth = data.get_buff_path()
            self.encoder.play_buff(bfpth)

            if(data.get_type() == self.variables.FIFO_TYPE_IMG()):
                os.system('rm '+data.get_path())

            os.system('rm '+bfpth) 
        except IndexError : 
            print('Index Error')
    
    def pop_all(self):
        dequelen = len(self.fifo)
        for i in range(dequelen):
            self.pop()

    def get_fifo(self): 
        return self.fifo

    def get_fifo_list(self): 
        txt_count = 0 
        img_count = 0
        for i in self.fifo:
            if(i.get_type() == self.variables.FIFO_TYPE_TXT()):
                txt_count = txt_count + 1
            else:
                img_count = img_count + 1

        msg = 'TXT;'+str(txt_count)+';IMG;'+str(img_count)
        txdt = text_data(variables = self.variables)
        txdt.set_date(self.date_time.get_time_utc_str())
        txdt.set_text(message=msg)
        self.append_left(txdt) 
        self.pop()

    def construct_picture(self, **kwargs): 
        pc = picture_data(variables = self.variables) 
        pc.set_date(kwargs['datetime'])
        pc.set_path(kwargs['path']) 
        self.append(pc)

        txt = text_data(variables = self.variables)
        txt.set_date(kwargs['datetime'])
        txt.set_text(image_date = kwargs['datetime'], alt=kwargs['alt'])
        self.append(txt)

    def construct_message(self, message): 
        txt = text_data(variables = self.variables)
        txt.set_date(self.date_time.get_time_utc_str()) 
        txt.set_text(message=message) 
        self.append(txt)
