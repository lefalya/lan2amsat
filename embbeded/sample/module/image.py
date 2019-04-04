import os
import cv2
import PIL.Image
from resizeimage import resizeimage 
from datetime import datetime 

class image: 

    def __init__(self, mode):
        self.cv2_filename = "opencv_cam.jpg"
        self.mode = mode

    def transmit(self, image_path, mode):
        with open(image_path, 'r+b') as f: 
            with PIL.Image.open(f) as image : 
                cover = resizeimage.resize_cover(image, self.get_size(mode))
                cover.save("./capture/cap_res.jpg", image.format)

        os.system("./shell/send_sstv.sh ../capture/cap_res.jpg "+mode)
   
    def get_size(self,mode): 
        return {
                'Robot36' : [320,240],
                'Robot8BW' : [160, 120] 
            }[mode]

    def capture(self):
        time = datetime.utcnow()
        formated_time = time.strftime('%B %d %Y - %H:%M:%S:%f')
        filename = time.strftime('%B_%d_%Y_%H_%M_%S_%f')
        filename = filename + '.jpg'
        path = './capture/'+filename 
        camera = cv2.VideoCapture(0) 
        return_val, img = camera.read() 
        cv2.imwrite(path, img) 

        return path, formated_time

if __name__ == "__main__" : 
    image_client = image('Robot36')
#    image_client.transmit(sstv_client,'../assets/500x500.jpg', 'Robot36')
    path, time = image_client.capture()    
    print(path)
    print(time)

