from datetime import datetime 
from skyfield.api import Topos, load 
from _thread import * 

import threading 
import select 
import socket 

print_lock = threading.Lock()
def recv_data():
    while True : 
        
        buff = connect_direwolf.recv(1024) 
        if not buff: 
            print('bye') 
            print_lock.release()
            break 

        #buff = buff[::-1]
        buff = buff.decode('ISO-8859-1')
        buff = buff.split("\xf0")
        buff = buff[1]
        buff = buff[0:(len(buff)-1)] 

def get_az_el(): 

    el_last = ''
    TLE = 'http://www.celestrak.com/NORAD/elements/active.txt'
    satellites = load.tle(TLE) 
    satellite = satellites['LAPAN-A2']
    print(satellite)

    #recv = Recv('localhost', 8001)

    while True : 
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

#    if select.select([recv], [],[],1)[0]:
#    print(recv.read())

        if str(el) != el_last : 
            print(el, az, distance.km)
            el_last = str(el)

if __name__ == "__main__": 

    connect_direwolf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect_direwolf.connect(('localhost', 8001)) 

    while True : 
        print_lock.acquire()
        start_new_thread(get_az_el, ())
        start_new_thread(recv_data, ())

    
    

