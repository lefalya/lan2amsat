import os
import cv2
from PIL import Image
from resizeimage import resizeimage 

class Image: 

    cv2_filename = "opencv_cam.jpg"

    def transmit(self, image_path, mode):
        with open(image_path, 'r+b') as f: 
            with Image.open(f) as image : 
                cover = resizeimage.resize_cover(image, self.get_size(mode))
                cover.save("capture/cap_res.jpg", image.format)

        os.system("./shell/send_sstv.sh cap_res.jpg "+mode)
   
    def get_size(mode): 
        return {
                'Robot36' : [320,240],
                'Robot8BW' : [160, 120] 
            }[mode]

    def capture(self, mode) :
        
        camera = cv2.VideoCapture(0) 
        return_val, img = camera.read() 
        print(img)
        #cv2.imwrite("./capture/"+self.cv2_filename,img) 
        #self.transmit(self, "./capture/"+self.cv2_filename, mode) 

if __name__ == "__main__" : 
    image_client = Image
#    image_client.transmit(sstv_client,'../assets/500x500.jpg', 'Robot36')
    image_client.capture(image_client, 'Robot36')    

