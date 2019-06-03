import os
import cv2
import PIL.Image
from resizeimage import resizeimage 
import date_time 

class image: 

    def __init__(self, **kwargs):
        self.cv2_filename = "opencv_cam.jpg"
        self.mode = kwargs['mode']

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
        formated_time = date_time.get_time_utc_str()
        filename = date_time.get_time_utc_filename()
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

