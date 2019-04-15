from datetime import datetime 

class event : 
    def __init__(self):
        self.type = '' 
        self.date = '' 
        self.buff_path = '' 

    def set_type(self, type_name): 
        self.type = type_name

    def set_buff_path(self, path):
        self.buff_path = path

    def set_date(self, date_time): 
        self.date = date_time 

    def get_type(self):
        return self.type 

    def get_date(self): 
        return self.date

    def get_buff_path(self): 
        return self.buff_path
