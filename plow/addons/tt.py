
from PIL import Image, ImageDraw, ImageFont
new_img = Image.new('RGB', (730, 120), (0, 0, 0, 0))
pencil = ImageDraw.Draw(new_img)
main_info = ImageFont.truetype('PRFW.TTF', 120)
pencil.text((0, 0), "PT99399239", (41, 37, 43), font=main_info)

new_img.save('im.png')
