import cv2

class imgTransform:
    
    def __init__(self, imgPath):
        super().__init__()
        self.img_src = cv2.imread(imgPath)
    
    def show(self):
        return self.img_src
        
    def convert(self, img, color):
        if color == 'gray' or color == 'GRAY':
            return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            pass
    
        