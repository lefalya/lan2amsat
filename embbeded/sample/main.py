from skyfield.api import Topos, load 
from collections import deque 
from scipy.constants import c

from module import direwolf 
from module import gqrx 
from module import tle
from module import Tracker 
from module import date_time 

from task import task_runner
from inout import io_handler 
from fifo import fifo 

#import schedule
import threading 
import select 
import socket 
import os

# distance between station and passing satellite 
dis = 0 

# theading lock 
print_lock = threading.Lock()
    
# satellite center frequency 
center_frequency = 435880000 #Hz

class main : 
    
    def __init__(self):
        self.distance = 0 
        self.callsign = "GSRASP"
        self.sstv_mode = "Robot36"
        self.calculate_az_el = True
        
        ''' 
        datetime -> io_handler -> camera_handler -> image'
        '''
        self.io = io_handler(datetime = date_time) 
        
        ''' 
        callsign -> fifo -> encoder'  
        variables -> fifo' -> encoder'
        datetime -> fifo' 
        '''
        self.fifo = fifo(callsign = self.callsign)
        self.fifo.set_master_io(self.io) # Rule [1] 
        self.io.set_master_fifo(self.fifo) # Rule [1]

        ''' 
        mode -> camera_handler -> image' 
        '''
        self.io.set_camera_handler(mode = self.sstv_mode) # Rule [2]
        self.io.set_serial_handler() # Rule [2] 
        '''
        main -> task_runner' 
        '''
        self.task = task_runner(
                main = self,
                callsign = self.callsign,
                fifo = self.fifo,
                io = self.io,
                mode = self.sstv_mode
                )

        self.tracker = Tracker(
                latitude = '6.2405 S',
                longitude = '106.9501 E')

    def set_frequency(self) : 
        radio.correct_doppler(self.distance)

    def get_fifo(self):
        return self.fifo.encode_thread()

    def recv_data(self):
        while True :
            receive = rx.receive()
            if receive.closed == True : 
                print_lock.release()
                break

            self.task.parse_command(receive.callsign, receive.message)

    def main_thread(self): 

        global dis 
        
        append_status = False

        # last elevation
        el_last = ''
        while True :          
            
            self.io.read_serial()
            self.fifo.encode_thread()    
            if self.calculate_az_el :  
                el,az,dis = self.tracker.track()
                self.distance = dis 

                #append first distance 
                if(not append_status):
                    self.set_frequency()
                    append_status = True 

                if str(el) != el_last :
                    self.tracker.print_azeldis() 
                    self.set_frequency()
                    print('FIFO Contents : ', self.fifo.fifo) 
                    print('ENCODE_BUFF Contents : ', self.fifo.encode_buff)                 
                    el_last = str(el)

if __name__ == "__main__": 

    run = main()
    rx = direwolf('localhost', 8001)
    radio = gqrx(center_frequency)  

    print('RUNNING')
    print_lock.acquire()
    p1 = threading.Thread(target=run.main_thread, args=()) 
    p2 = threading.Thread(target=run.recv_data, args=())
    p1.start()
    p2.start()

    
    

