import os
from PIL import Image

class ImageToPdf(object):
    def __init__(self,imagePath):
        self.imagePath = imagePath
        self.fileName = str(imagePath.split("\\")[-1])
        
        
    def convert(self):
        try:
            newFile = os.path.join(self.imagePath.replace(self.fileName.split(".")[-1], "pdf"))
            image_file = Image.open(self.imagePath)
            result = image_file.convert("RGB")
            result.save(newFile)
            print("Convertion Successful..")
        except:   
            print("Convertion Unsuccessful..")

if __name__ == "__main__":
    image = input(r"Drag picture here >> ")
    ImageToPdf(image).convert()