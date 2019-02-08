import socket 

class Recv: 

    def __init__(self, ip, port): 
        self.buff = "" 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.socket.connect((ip, port))
        self.socket.setblocking(0)

    def read(self, length = 1024):
        return self.socket.recv(length) 

    def read_until(self, data): 
        if not data in self.buff: 
            self.buff += self.socket.recv(1024) 

        pos = self.buff.find(data) 
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):] 
