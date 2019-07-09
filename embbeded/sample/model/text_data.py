from model import event 
from model import variables

class text_data(event): 

    def __init__(self, **kwargs): 
        self.text = '' 
        self.set_type(variables.FIFO_TYPE_TXT())
        self.callsign = ''

    def set_callsign(self, callsign):
        self.callsign = callsign

    def set_text(self, **kwargs): 
        text = '' 
        if 'image_date' in kwargs :
            text = 'IMGDT;DT;'+kwargs['image_date']+';ALT;'+kwargs['alt']
        else : 
            text = self.callsign+';'+kwargs['message']
        
        self.text = text

    def get_text(self): 
        return self.text 

