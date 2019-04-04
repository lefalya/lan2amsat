from datetime import datetime 
from module import image

class camera_handler : 
    def __init__(self, fifo): 
        self.thold_start = datetime.utcnow()
        self.image = image('Robot36')
        self.master_fifo = fifo 

    def trigger(self): 
        dt = datetime.utcnow() 
        interval = (dt - self.thold_start).total_seconds()
        if (interval > 5):
            self.thold_start = dt 
            
            path, time = self.image.capture()
            self.master_fifo.construct_picture(
                    path = path, 
                    alt = time
                )

