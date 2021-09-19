from PIL import Image, ImageDraw, ImageFont
label = 'PT99399239'
font = ImageFont.truetype('PRFW.TTF', 120)
line_height = sum(font.getmetrics())  # в нашем случае 33 + 8 = 41

fontimage = Image.new('L', (font.getsize(label)[0], line_height))
# И рисуем на ней белый текст
ImageDraw.Draw(fontimage).text((0, 0), label, fill=255, font=font)
fontimage = fontimage.rotate(90, resample=Image.BICUBIC, expand=True)
orig = Image.open('ukraine_inernational.jpg')
orig.paste((41, 37, 43), box=(30, 180), mask=fontimage)

orig.show()
