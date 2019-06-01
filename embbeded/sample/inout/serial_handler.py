
class serial_handler :
    def __init__(self, **kwargs):
        self.master_io = kwargs['master_io']
        self.master_fifo = kwargs['master_fifo']

    def parse(self, data):
        if b';' in data:
            data = data.split(b';')
            print(data)
            com = data[0]
            msg = data[1] 
            self.com_w_msg(com, msg) 
    
    def com_wt_msg(self, com): 
        print('a') 

    def com_w_msg(self, com, msg): 
        if com == b'MSG': 
            msg = msg.decode('utf-8')
            self.master_fifo.construct_message(
                    message=msg) 


