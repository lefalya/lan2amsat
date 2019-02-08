import base64
import os 
class Image :
    
    def encode(image, baud): 
        encoded_string = base64.b64encode(open(image,'rb').read())
        total_count = 0 
        count = 0 
    #    b64 = ''
        os.system("./generate.sh '"+open(image,'rb').read()+"' '"+baud+"'")
        
        for i in encoded_string.decode('utf-8') : 
            count += 1
            b64 += i 
            total_count += 1
            if count == 2000 or total_count == len(encoded_string): 
                print(b64)
                os.system("./generate.sh '"+b64+"' '"+baud+"'")
                b64 = '' 
                count = 0 

class sstv: 
    def encode(image_path, mode): 
        os.system("./generate.sh "+image_path+" "+mode)
    
if __name__ == "__main__" : 
    encoder = sstv
    encoder.encode('640x480.jpg', 'Robot36')

