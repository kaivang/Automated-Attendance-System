from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)
images = convert_from_path('test5.pdf')

for i,image in enumerate(images): 
   fname = 'test'+str(i)+'.jpg'
   image.save(fname, "JPEG")
   image.show()
   
