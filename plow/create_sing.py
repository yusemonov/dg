from PIL import Image
from glob import glob
from pathlib import Path


def create_sing():
    for images in glob('sings/*.jpg'):
        name_img = Path(images).name
        print(name_img)
        img = Image.open(images).convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] > 70 and item[1] > 70 and item[2] > 70:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save("sing_png/" + name_img + ".png")
        print("Successful")


create_sing()
