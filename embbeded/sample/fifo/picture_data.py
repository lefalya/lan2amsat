from fifo import fifo_data

class picture_data(fifo_data.fifo_data): 

    def __init__(self):
        self.path = '' 
        self.alt = '' 

    def set_path(self, path): 
        self.path = path 

    def set_alt(self,alt):
        self.alt = alt 

    def get_path(self):
        return self.path 

    def get_alt(self): 
        return self.alt 
