from skyfield.api import Topos, load
from module import tle 
from datetime import datetime 

class Tracker : 
    def __init__(self, **kwargs): 
        self.latitude = kwargs['latitude']
        self.longitude = kwargs['longitude']

        self.satellite = '' 
        self.el = ''
        self.az = '' 
        self.dis = '' 

    def track(self): 
        tl = tle()
        self.satellite = tl.satellite

        ts = load.timescale()
        t = ts.utc(datetime.utcnow().year,
                datetime.utcnow().month,
                datetime.utcnow().day,
                datetime.utcnow().hour,
                datetime.utcnow().minute,
                datetime.utcnow().second)

        my_location = Topos(self.latitude, self.longitude)
        difference = self.satellite - my_location
        topocentric = difference.at(t)
        el,az,distance = topocentric.altaz()
        d = distance.m

        self.el = el 
        self.az = az 
        self.dis = d

        return el,az,d
    
    def print_azeldis(self): 
        print("\n")
        print(self.satellite)
        print("elevation    : ", self.el)
        print("azimuth      : ", self.az) 
        print("slant range  : ", self.dis)

