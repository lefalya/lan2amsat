from collections import deque 
from model import picture_data
from model import text_data 
from model import variables
from module import encoder
from module import date_time
import os 
import time

class fifo: 
    
    def __init__(self, **kwargs): 

        # FIFO 
        self.fifo = deque()
        self.callsign = kwargs['callsign'] 

        # Encode Buffer 
        self.encode_buff = deque()

        # Injected instance, apply rule [2] 
        self.master_io = ''         

        self.encoder = encoder(callsign = kwargs['callsign'])

    # Inter-dependent class, apply rule [1] 
    def set_master_io(self, master_io): 
        self.master_io = master_io 

    def encode_thread(self):
        if len(self.encode_buff) > 0:
            data = self.encode_buff.popleft() 
            wav_buff_path = self.encoder.generate_buff(data) 
            data.set_buff_path(wav_buff_path) 

            if (data.get_live() == True):
                print('live command')
                self.fifo.appendleft(data)
                self.master_io.ptt_high()
                time.sleep(0.5)
                self.pop()
                self.master_io.ptt_low()
            else:
                self.fifo.append(data)

    def pop(self):
        try :
            data = self.fifo.popleft() 
            bfpth = data.get_buff_path()

            # transmit buffer
            self.encoder.play_buff(bfpth)

            if(data.get_type() == variables.FIFO_TYPE_IMG()):
                os.system('rm '+data.get_path())

            os.system('rm '+bfpth) 
        except IndexError :
            message = '400'
            self.construct_message(
                    message=message,
                    live=True)
            print('Index Error')
    
    def pop_all(self):
        dequelen = len(self.fifo)
        self.master_io.ptt_high()
        time.sleep(0.5)
        for i in range(dequelen):
            self.pop()
        self.master_io.ptt_low()

    def get_fifo(self): 
        return self.fifo

    def get_fifo_list(self): 
        txt_count = 0 
        img_count = 0
        for i in self.fifo:
            if(i.get_type() == variables.FIFO_TYPE_TXT()):
                txt_count = txt_count + 1
            else:
                img_count = img_count + 1

        msg = 'TXT;'+str(txt_count)+';IMG;'+str(img_count)
        txdt = text_data()
        txdt.set_date(date_time.get_time_utc_str())
        txdt.set_text(message=msg)
        txdt.set_live(True)

        self.encode_buff.append(txdt)

    def construct_picture(self, **kwargs): 
        pc = picture_data() 
        pc.set_date(kwargs['datetime'])
        pc.set_path(kwargs['path'])
        txt = text_data()
        txt.set_date(kwargs['datetime'])
        txt.set_text(image_date = kwargs['datetime'], alt=kwargs['alt'])

        if 'live' in kwargs:
            pc.set_live(True)
            txt.set_live(True)
        else: 
            pc.set_live(False) 
            txt.set_live(False)

        self.encode_buff.append(pc)
        self.encode_buff.append(txt)

    def construct_message(self, **kwargs): 
        txt = text_data()
        txt.set_date(date_time.get_time_utc_str()) 
        txt.set_text(message=kwargs['message']
                +";"
                +self.callsign)

        if 'live' in kwargs:
            txt.set_live(True)
        else: 
            txt.set_live(False)

        self.encode_buff.append(txt)
