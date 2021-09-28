import qrcode
from PIL
import Image
import matplotlib.pyplot as plt
from PIL
import ImageDraw
from PIL
import ImageFont
def getQRcode(strs, name):
  qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 2,
  )
qr.add_data(strs)
qr.make(fit = True)
img = qr.make_image(fill_color = "black", back_color = "white")
img = img.convert("CMYK") # RGBA
icon = Image.open("tco.jpg")
img_w, img_h = img.size
factor = 6
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
if icon_w > size_w:
  icon_w = size_w
if icon_h > size_h:
  icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
img.paste(icon, (w, h), None)
img = img.convert('RGB')
img.save(name)
return img
def info(name, body):
  getQRcode(body, name)
oriImg = Image.open("backgroud.jpg")
oriImg2 = Image.open(name)
oriImg2 = oriImg2.resize((490, 490))
oriImg.paste(oriImg2, (80, 80))
draw = ImageDraw.Draw(oriImg)
oriImg = oriImg.convert('RGB')
oriImg.save(name)
if __name__ == '__main__':
  info("qrcode_result.png", "https://www.web,whatsapp.com")
