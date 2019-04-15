import os
import cv2
import PIL.Image
from resizeimage import resizeimage 
from datetime import datetime 

class image: 

    def __init__(self, mode):
        self.cv2_filename = "opencv_cam.jpg"
        self.mode = mode

    def resize(self, image_path, mode):
        with open(image_path, 'r+b') as f: 
            with PIL.Image.open(f) as image : 
                cover = resizeimage.resize_cover(image, self.get_size(mode))
                cover.save(image_path, image.format)

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
        self.resize(path, self.mode)
        return path, formated_time

if __name__ == "__main__" : 
    image_client = image('Robot36')
    path, time = image_client.capture()    
    print(path)
    print(time)

