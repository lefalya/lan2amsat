import base64
import os 

class Image : 
    def encode(image): 
        encoded_string = base64.b64encode(open(image,'rb').read())
        total_count = 0 
        count = 0 
        b64 = ''
        for i in encoded_string.decode('utf-8') : 
            count += 1
            b64 += i 
            total_count += 1
            if count == 300 or total_count == len(encoded_string): 
                print(b64)
                os.system("./generate.sh '"+b64+"'")
                b64 = '' 
                count = 0 
                
if __name__ == "__main__" : 
    encoder = Image
    encoder.encode('toulouse.jpg')
