import os
import cv2
import PIL.Image
from resizeimage import resizeimage 

class image: 

    def __init__(self, mode, fifo):
        self.cv2_filename = "opencv_cam.jpg"
        self.mode = mode
        self.fifo = fifo

    def transmit(self, image_path, mode):
        with open(image_path, 'r+b') as f: 
            with PIL.Image.open(f) as image : 
                cover = resizeimage.resize_cover(image, self.get_size(mode))
                cover.save("../capture/cap_res.jpg", image.format)

        os.system("../shell/send_sstv.sh ../capture/cap_res.jpg "+mode)
   
    def get_size(self,mode): 
        return {
                'Robot36' : [320,240],
                'Robot8BW' : [160, 120] 
            }[mode]

    def capture(self):
        print("capture !")        
        camera = cv2.VideoCapture(0) 
        return_val, img = camera.read() 
        cv2.imwrite("../capture/"+self.cv2_filename,img) 
        self.transmit("../capture/"+self.cv2_filename, self.mode) 

if __name__ == "__main__" : 
    image_client = image('Robot36', '')
#    image_client.transmit(sstv_client,'../assets/500x500.jpg', 'Robot36')
    image_client.capture()    

