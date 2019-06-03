# APRS and SSTV encoder 

# For testing purpose
from model import picture_data
import os 
from datetime import datetime
from model import variables

class encoder : 

    def __init__(self, **kwargs): 
        self.callsign = kwargs['callsign']

    def encode_aprs(self, text):
        file_name = "./buff/aprs_wav_"+text.get_date().replace(' ','_')+'.wav'
        com = "echo -n '"+self.callsign+">WORLD:"+text.get_text()+"' | gen_packets -a 100 -o "+file_name+" -"        
        os.system(com)

        return file_name

    def encode_sstv(self, picture):
        img_path = picture.get_path()
        img_date = picture.get_date()
        wav_path = "./buff/sstv_wav_"+img_date.replace(' ','_')+'.wav'
        com = 'python -m pysstv '+img_path+' '+wav_path+' --mode Robot36'
        os.system(com)
        return wav_path

    def generate_buff(self, data):
        bf_path = ''
        if (data.get_type() == variables.FIFO_TYPE_IMG()):
            bf_path = self.encode_sstv(data) 
        elif (data.get_type() == variables.FIFO_TYPE_TXT()): 
            bf_path = self.encode_aprs(data)
        else :
            print('type not defined')

        return bf_path

    def play_buff(self, buff_path):
        os.system('play '+buff_path)
