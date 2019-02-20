from datetime import datetime 
from skyfield.api import Topos, load 
from _thread import * 
from collections import deque 
from scipy.constants import c

from module import direwolf 
from module import gqrx 
from task_runner import task_runner

import schedule
import threading 
import select 
import socket 

# distance between station and passing satellite 
dis = 0 

# satellite elevation 

# queue dis 
qdis = deque(maxlen=2)

# theading lock 
print_lock = threading.Lock()
    
# delta time in second 
deltaT = 1 

# satellite center frequency 
center_frequency = 435880000 #Hz

class main : 
    
    def __init__(self):
        self.distance = 0 
        self.callsign = "YDE2E"
        self.task = task_runner(self.callsign)
        self.sstv_mode = "Robot36"

    def set_frequency(self) : 
        radio.get_corrected_frequency(self.distance)

    def recv_data(self):
        while True : 
            receive = rx.receive()
            if receive.closed == True : 
                print_lock.release()
                break

            self.task.parse_command(receive.callsign, receive.message)

    def get_az_el(self): 

        global dis, deltaT
        
        append_status = False

        # last elevation
        el_last = ''

        # satellite's  obital element 
        TLE = 'http://www.celestrak.com/NORAD/elements/active.txt'

        # load all listed satellites 
        satellites = load.tle(TLE) 

        # get LAPAN-A2 TLE 
        satellite = satellites['LAPAN-A2']
        print(satellite)
        
        schedule.every(deltaT).seconds.do(self.set_frequency)

        while True : 
            schedule.run_pending()
            ts = load.timescale() 
            t = ts.utc(datetime.utcnow().year, 
                       datetime.utcnow().month, 
                       datetime.utcnow().day, 
                       datetime.utcnow().hour, 
                       datetime.utcnow().minute, 
                       datetime.utcnow().second) 
            my_location = Topos('6.2405 S', '106.9501 E') 
            difference = satellite - my_location
            topocentric = difference.at(t) 
            el,az,distance = topocentric.altaz()
            self.distance = distance.m

            #append first distance 
            if(not append_status):
                self.set_frequency()
                append_status = True 

            if str(el) != el_last :
                print("\n")
                print(el, az, distance.m)
                el_last = str(el)

if __name__ == "__main__": 

    run = main()
    rx = direwolf('localhost', 8001)
    radio = gqrx(center_frequency, deltaT)  
    while True : 
        print_lock.acquire()
        start_new_thread(run.get_az_el, ())
        start_new_thread(run.recv_data, ())

    
    
