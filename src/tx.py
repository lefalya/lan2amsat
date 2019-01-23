import base64 
import sys 
import os 

encoded_string = base64.b64encode(open(sys.argv[1],'rb').read())
encoded_to_string = encoded_string.decode('utf-8')
os.system("echo '"+encoded_to_string+"' | minimodem --tx 4800")

