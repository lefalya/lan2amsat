import subprocess
import select
import time 

class recv: 
    packet = ''
    in_packet = False 
    def __init__(self, baud): 

        self.result = subprocess.Popen(['minimodem', '--rx', baud], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def getpacket(self):
        while True :
            readers, _, _ = select.select([self.result.stdout, self.result.stderr],[],[])
            if self.in_packet:
                if self.result.stdout in readers:
                    data = self.result.stdout.read(1) 
                    if not data: 
                        break 
                    self.packet += data.decode('ISO-8859-1')
                    continue 
            if self.result.stderr in readers:
                line = self.result.stderr.readline()
#                print(line)
                if not line: 
                    break
                if line.startswith(b'### CARRIER '):
                    self.in_packet = True
                    self.packet = ''
                elif line.startswith(b'### NOCARRIER '):
                    #print('end')
                    self.in_packet = False
            print (self.packet)
            time.sleep(1)
                
