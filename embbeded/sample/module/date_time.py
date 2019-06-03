from datetime import datetime 

class date_time: 

    def get_time_utc(): 
        dt = datetime.utcnow() 
        return dt 

    def get_time_utc_str():
        dt = datetime.utcnow() 
        rt = dt.strftime('%B %d %Y - %H:%M:%S:%f') 
        return rt 

    def get_time_utc_filename(): 
        dt = datetime.utcnow() 
        rt = dt.strftime('%B_%d_%Y_%H_%M_%S_%f')
        return rt 

    def get_time(): 
        dt = datetime.now()
        return dt 

    def get_time_str(): 
        dt = datetime.now() 
        rt = dt.strftime('%B %d %Y - %H:%M:%S:%f')
        return rt

    def get_time_filename(): 
        dt = datetime.now()
        rt = dt.strftime('%B_%d_%Y_%H_%M_%S_%f')
        return rt

    

