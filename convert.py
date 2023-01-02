from cv2 import (
    IMREAD_UNCHANGED,
    cvtColor,
    COLOR_RGB2GRAY,
    bitwise_not,
    GaussianBlur,
    divide,
    imwrite,
    imdecode
)

from numpy import fromstring, uint8


class Sketch:
    def __init__(self,fileobject) -> None:
        self.fileobject = fileobject
    

    def convert(self,filename):
        self.image_read = imdecode(fromstring(self.fileobject.read(),uint8), IMREAD_UNCHANGED)
        self.gray_image = cvtColor(self.image_read,COLOR_RGB2GRAY)
        self.invert_img = bitwise_not(self.gray_image)
        self.blur_image = GaussianBlur(self.invert_img, (111,111),0)
        self.invertblur = bitwise_not(self.blur_image)
        self.sketch_img = divide(self.gray_image,self.invertblur,scale=256.0)
        imwrite(filename,self.sketch_img)