import pytesseract        
from PIL import Image      
import pyttsx3            
from googletrans import Translator       

img = Image.open('text1.png')      
print(img)                           
pytesseract.pytesseract.tesseract_cmd ='/usr/local/Cellar/tesseract/4.1.1/bin/'   
result = pytesseract.image_to_string(img)    
with open('abc.txt',mode ='w') as file:
                 file.write(result) 
                 print(result) 
                   
p = Translator()                       
# translates the text into german language 
k = p.translate(result,dest='german')       
print(k) 
engine = pyttsx3.init() 
  
# an audio will be played which speaks the test if pyttsx3 recognizes it 
engine.say(k)                              
engine.runAndWait()