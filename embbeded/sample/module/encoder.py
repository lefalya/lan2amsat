# APRS and SSTV encoder 

# For testing purpose
from model import picture_data
import os 

class encoder : 

    def __init__(self, callsign): 
        self.callsign = callsign

    def encode_aprs(self, text):
        file_name = "./buff/aprs_wav_"+text.get_date().replace(' ','_')+'.wav'
        com = "echo -n '"+self.callsign+">WORLD:"+text.get_text()+"' | gen_packets -a 100 -o "+file_name+" -"        
        print(com)
        os.system(com)

        return file_name

    def encode_sstv(self, picture):
        img_path = picture.get_path()
        img_date = picture.get_date() 
        wav_path = "./buff/sstv_wav_"+img_date.replace(' ','_')+'.wav'
        com = 'python -m pysstv '+img_path+' '+wav_path+' --mode Robot36'
        os.system(com)

        print(wav_path)
        print(com)

        return wav_path

    def generate_buff(self, data):
        bf_path = ''
        if (data.get_type() == 'img'):
            bf_path = self.encode_sstv(data) 
        elif (data.get_type() == 'msg') : 
            bf_path = self.encode_aprs(data)
        else :
            print('type not defined')

        return bf_path

    def play_buff(self, buff_path):
        print('path '+buff_path)
        os.system('play '+buff_path)
