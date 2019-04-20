from datetime import datetime 
from module import image

class camera_handler : 
    def __init__(self, **kwargs): 
        self.thold_start = datetime.utcnow()
        self.image = image(
                mode = kwargs['mode'], 
                datetime = kwargs['datetime'])

        # apply rule [2] 
        # non inter-dependent instances, ignoring rule [1] 
        self.master_fifo = kwargs['fifo'] 

    def trigger(self): 
        dt = datetime.utcnow() 
        interval = (dt - self.thold_start).total_seconds()
        if (interval > 5):
            self.thold_start = dt 
            
            print('IO : INTERRUPT CAMERA PIN 12')
            path, time = self.image.capture()
            self.master_fifo.construct_picture(
                    path = path,
                    datetime = time,
                    alt = time # Soon via UART
                )

