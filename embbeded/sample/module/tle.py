import os 
from skyfield.api import load 
from logic import read_tle 

class tle : 

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.TLE = '/../active.txt'
        self.TLE_path = ''.join([self.path + self.TLE])
        self.satellites = load.tle(self.TLE_path) 
        self.satellite = self.satellites['LAPAN-A2']
        self.test_string = "myfirststring" 
        self.read_tle = read_tle()
        
    def satellite(self):
        return self.satellite

    def printString(self): 
        print(self.test_string)

    def setString(self, txt): 
        self.test_string = txt

    def set_tle(self, tle): 
        tle_file = open(self.TLE_path, "w+") 
        decoded_tle = self.read_tle.decode(tle) 
        for column in decoded_tle: 
            tle_file.write(column)
            tle_file.write("\n")
        tle_file.close()

        os.remove(self.path+"/../Leap_Second.dat")
        os.remove(self.path+"/../deltat.data") 
        os.remove(self.path+"/../deltat.preds")

        
