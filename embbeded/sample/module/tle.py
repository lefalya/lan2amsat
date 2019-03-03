import os 
from skyfield.api import load 

class tle : 

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.TLE = '/../active.txt'
        self.TLE_path = ''.join([self.path + self.TLE])
        self.satellites = load.tle(self.TLE_path) 
        self.satellite = self.satellites['LAPAN-A2']
        self.test_string = "myfirststring" 
        
    def satellite(self):
        return self.satellite

    def printString(self): 
        print(self.test_string)

    def setString(self, txt): 
        self.test_string = txt

