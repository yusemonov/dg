from PIL import Image

SOURCE_DIR = 'Admin/'

# one = Image.open(SOURCE_DIR + '7.jpg').convert('RGBA')
# one.putalpha(180)
# # one.save('test.png')
# # img_new = Image.new('L', one.size, (0, 0, 255))
# # r, g, b, a = one.split()
# # one.putalpha(0)
# one.save('sing.png', format='PNG')

img = Image.open(SOURCE_DIR + '7.jpg')
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in range(height):
    for x in range(width):
        if pixdata[x, y] == (255, 255, 255, 0):
            pixdata[x, y] = (0, 0, 0, 255)

img.save('neeew.png', "PNG")
