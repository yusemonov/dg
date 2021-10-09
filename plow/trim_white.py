from PIL import Image, ImageOps

image = Image.open("Admin/7.jpg")
image.load()
imageSize = image.size
invert_im = image.convert("RGBA")
invert_im = ImageOps.invert(invert_im)
imageBox = invert_im.getbbox()
cropped = image.crop(imageBox)
cropped.save("img.png")
