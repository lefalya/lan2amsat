from collections import deque 

class picture_fifo : 

    def __init__(self):
        self.pictures = deque()

    def append(picture):
        self.pictures.append(picture) 

    def pop(): 
        try : 
            self.pictures.popleft() 
        except IndexError : 
            print("Empty FIFO")

    def get_size(): 
        return len(self.pictures)
