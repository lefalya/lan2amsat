from scipy.constants import c 
from collections import deque 
import telnetlib 

class gqrx : 
    def __init__(self, center_frequency, delta_t): 
        self.center_frequency = center_frequency
        self.delta_t = delta_t 
        self.distance_deque = deque(maxlen=2)
        self.gqrx = telnetlib.Telnet("127.0.0.1", 7356) 

    def calculate_corrected_frequency(self,distance):
        self.distance_deque.append(distance) 
        if(len(self.distance_deque) == 2):
            relative_velocity = (self.distance_deque[1]-self.distance_deque[0])/self.delta_t 
            delta_f = relative_velocity * self.center_frequency/c 
            corrected_frequency = (self.center_frequency + (-1*delta_f))

            print("doppler : ", -1*delta_f)
            print("corrected freq : ", corrected_frequency)
            return corrected_frequency 

    def correct_doppler(self, distance):
        freq = self.calculate_corrected_frequency(distance)
        if type(freq) != type(None) : 
            freq = str(round(freq)).split(".")[0]
            self.gqrx.write(("F "+freq+" \n").encode('ascii'))
