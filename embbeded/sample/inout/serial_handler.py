from collections import deque 

class serial_handler :
    def __init__(self, **kwargs):
        self.master_io = kwargs['master_io']
        self.master_fifo = kwargs['master_fifo']
        
        self.inCommand = ''
        self.buffer = ''

        self.deque = deque(maxlen=3)
    
    def parse(self,data):
        self.enableBuffer(data) 
        self.deque.append(data) 
        if len(self.deque) == 3:
            self.splitter(b''.join(self.deque))

    def enableBuffer(self,data):
        if self.inCommand != '':
            self.buffer = self.buffer+data.decode('utf-8')

    def splitter(self, com):
        com = com.decode('utf-8')

        if com == "MSL":
            self.inCommand="MSL"

        elif com == "END":
            self.buffer = self.buffer.replace('END', '')
            self.execute(command=self.inCommand, message=self.buffer)
            self.inCommand = ''
            self.buffer = ''

    def execute(self, **kwargs):
        if 'message' in kwargs : 
            com = kwargs['command']
            if com == 'MSL':
                self.master_fifo.construct_message(
                        message="MSL@@@"+kwargs['message'],
                        live=True) 
            elif com == 'MSG':
                self.master_fifo.construct_message(
                        message="MSG@@@"+kwargs['message'])
