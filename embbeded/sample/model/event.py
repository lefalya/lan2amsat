from datetime import datetime 

class event : 
    def __init__(self):
        self.type = '' 
        self.date = '' 

    def set_type(self, type_name): 
        self.type = type_name 

    def set_date(self, date_text): 
        self.date = datetime.utcnow().strftime('%B %d %Y - %H:%M:%S')

    def get_type(self):
        return self.type 

    def get_date(self): 
        return self.date
