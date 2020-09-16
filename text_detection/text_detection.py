import pytesseract as pt 
pt.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

from PIL import Image 
img =  Image.open ("/Users/haris/Desktop/test.jpg")

text = pt.image_to_string(img)
print(text)