from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
import codecs

tool = pyocr.get_available_tools()[0]
print(tool)
#mylang = tool.get_available_languages()[0]
mylang = 'deu'
print(tool.get_available_languages())
builder = pyocr.builders.TextBuilder()

req_image = []
final_text = []

image_pdf = Image(filename="extractor/data/simple.pdf", resolution=300)
image_jpeg = image_pdf.convert('jpeg')

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        builder=builder
    )
    final_text.append(txt)
print(txt)

#txt = tool.image_to_string(
#    PI.open('a.tiff'),
#    lang=mylang,
#    builder=pyocr.builders.TextBuilder()
#    )
#print(txt)

