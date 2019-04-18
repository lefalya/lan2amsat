from model import event

class picture_data(event): 

    def __init__(self, **kwargs):
        self.path = ''
        self.alt = ''
        self.set_type(kwargs['variables'].FIFO_TYPE_IMG())

    def set_path(self, path): 
        self.path = path 

    def set_alt(self,alt):
        self.alt = alt 

    def get_path(self):
        return self.path 

    def get_alt(self): 
        return self.alt 
