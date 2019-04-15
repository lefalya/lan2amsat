from model import event 

class text_data(event): 

    def __init__(self): 
        self.text = '' 
        self.set_type('msg')

    def set_text(self, **kwargs): 
        text = '' 
        if 'image_date' in kwargs :
            text = 'IMGDT;DT;'+kwargs['image_date']+';ALT;'+kwargs['alt']
        else : 
            text = 'MSG;'+kwargs['message']
        
        self.text = text

    def get_text(self): 
        return self.text 

