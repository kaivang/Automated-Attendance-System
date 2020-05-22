import pytesseract       
  

from PIL import Image     
m=[]  
for i in range(1,7):
    img = Image.open('C:/Users/Kaivan/test/testing'+str(i)+'.jpg')
    result = pytesseract.image_to_string(img)
    print(result)
    m.append(result)    

    

