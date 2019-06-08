from skyfield.api import Topos, load
from astropy import units as u 
from module import tle 
from datetime import datetime 

class Tracker : 
    def __init__(self, **kwargs): 
        self.latitude = kwargs['latitude']
        self.longitude = kwargs['longitude']
        self.master_io = kwargs['master_io']

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

        self.el = self.formatDegree(el.to(u.deg))
        self.az = self.formatDegree(az.to(u.deg))
        self.dis = d
        
        return el,az,d
     
    def formatDegree(self, deg): 
        return '{0:0.03f}'.format(deg) 

    def print_azeldis(self): 
        print("\n")
        print(self.satellite)
        print("elevation    : ", self.el)
        print("azimuth      : ", self.az) 
        print("slant range  : ", self.dis)
    
    def set_an_tracker(self):
        # Send az el to antenna tracker 
        self.master_io.command_tracker(self.az, self.el)

