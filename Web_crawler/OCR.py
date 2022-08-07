import ddddocr
from PIL import Image
import io

ocr = ddddocr.DdddOcr()

with open("a.jpg", 'rb') as f:
    image = f.read()
    
# img = Image.open(io.BytesIO(image))
# print(img)
res = ocr.classification(image)
print(res)