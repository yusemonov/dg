import os
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS
from zipfile import ZipFile
import face_recognition
from mrz.generator.td3 import *
from transliterate import translit
from babel import Locale
import datetime
from babel.dates import format_date
from pathlib import Path
import random
import logging
logger = logging.getLogger(__name__)

MF = ImageFont.truetype('cfg/font/sans.ttf', 34)  # Основной шрифт
FFMRZ = ImageFont.truetype('cfg/font/cour.ttf', 47)  # Шрифт для MRZ
WIDTH = 440
SW = 440  # НАчальная ширина
SH = 1060
MFC = (40, 40, 40)  # Основной цвет шрифта


def dt(datestr):
    raw_da = datestr
    s = " "
    d = datetime.date(int(raw_da[0:2]), int(
        raw_da[2:4]), int(raw_da[4:6]))  # YYMMDD
    en_mouth = format_date(d, "MMM", locale='en')
    day = format_date(d, "d", locale='en')
    year = format_date(d, "yy", locale='en')
    ukr_date = format_date(d, "MMM", locale='uk')
    ukr_date_f = str(ukr_date)[0:3]
    done = str(day + s + ukr_date_f + "/" + en_mouth +
               s + year).replace(".", "/").upper()
    logger.info("Вызвана функция преобразования даты")
    return done


def write_main_data(mrz, save_after_main_data,  typedoc,  country,  passport_number,  surname,  given_name,  genre,  birth_date, data_start, exp_date, personal_number):
    """ Нанесение на шаблон документа основной информации """
    img = Image.open('cfg/template/uain.png')  # Шаблон паспорта

    draw = ImageDraw.Draw(img)

    draw.text((WIDTH, SH), str(typedoc), MFC,
              font=MF)  # Иип документа

    draw.text((WIDTH + 140, SH), str(country),
              MFC, font=MF)  # Страна выдачи

    draw.text((WIDTH + 489, SH),  passport_number, MFC,
              font=MF)  # Уникальный номер документа

    draw.text((WIDTH, SH + 67), str(surname + '/' + translit(surname,
                                                             'uk', reversed=True)).upper(), MFC,
              font=MF)  # Фамилия

    draw.text((WIDTH, SH + 134), str(given_name + '/' + translit(given_name,
                                                                 'uk', reversed=True)).upper(), MFC,
              font=MF)  # Имя влядельца документа

    draw.text((WIDTH, SH + 201),  'УКРАЇНА/UKRAINE',
              MFC, font=MF)  # Гражданство

    draw.text((WIDTH, SH + 268), str(dt(birth_date)),
              MFC, font=MF)  # Дата рождения

    ''' ПОЛ '''
    if genre == "M":
        g = 'Ч/M'
    else:
        g = 'Ж/F'
    draw.text((WIDTH, SH + 335), g, MFC, font=MF)  # Пол
    ''' end ПОЛ '''

    draw.text((WIDTH + 489, SH + 268), str(birth_date) +
              '-' + '1233', MFC, font=MF)  # Персональный номер

    draw.text((WIDTH + 160, SH + 335), str('м. Київ/UKR').upper(),
              MFC, font=MF)  # Город

    draw.text((WIDTH + 460, 770), str(personal_number).upper(), (178, 34, 34),
              font=ImageFont.truetype('media/cfg/font/sans.ttf', 40))

    draw.text((WIDTH, SH + 402), str(dt(data_start)),
              MFC, font=MF)  # Дата выдачи

    draw.text((WIDTH, SH + 469), str(dt(exp_date)),
              MFC, font=MF)  # Дата окончания
    draw.text((WIDTH + 489, SH + 402), '8099', MFC, font=MF)
    draw.text((60, SH + 650), str(mrz), MFC, font=FFMRZ)  # Добавляем mrz
    img.save(save_after_main_data)
    return save_after_main_data


def write_id(save_after_main_data_p, passport_number):
    passport_number = passport_number
    font = ImageFont.truetype('cfg/font/SNEgCheck1MP.ttf', 120)
    line_height = sum(font.getmetrics())  # в нашем случае 33 + 8 = 41
    fontimage = Image.new('L', (font.getsize(passport_number)[0], line_height))
    # И рисуем на ней белый текст
    ImageDraw.Draw(fontimage).text(
        (0, 0), passport_number, fill=120, font=font)
    fontimage = fontimage.rotate(90, resample=Image.BICUBIC, expand=True)
    orig = Image.open(save_after_main_data_p)
    orig.paste((67, 67, 67), box=(30, 180), mask=fontimage)
    orig.save(save_after_main_data_p)
    return save_after_main_data_p


def crop_face(img, path_to_save):
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(
        image, number_of_times_to_upsample=0, model="cnn")
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save(path_to_save)
        return path_to_save


def holohrama_paster(passport_temp_path, holo_path):
    passport_temp = Image.open(passport_temp_path).convert('RGBA')
    img = Image.open(holo_path)  # открываем файл голограммы
    wpercent = (500 / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((500, hsize), Image.ANTIALIAS)
    if img.mode != 'RGBA':
        alpha = Image.new('RGBA', (10, 10), 20)
        img.putalpha(alpha)
    paste_mask = img.split()[3].point(lambda i: i * 17 / 100.)
    passport_temp.paste(img, (140, SH + 310), mask=paste_mask)
    with_holo_path = f'media/cfg/tmp/passport{random.randint(1000,9999)}.png'
    passport_temp.save(with_holo_path)
    return with_holo_path


def paste_photo(passport_temp_path, pasport_photo_path, exif_infor, background_path):
    """Функция вставляет изображение в паспорт и добавляет фон

    Args:
        passport_temp_path ([type]): [description]
        pasport_photo_path ([type]): [description]
        exif_infor ([type]): [description]
        background_path ([type]): [description]

    Returns:
        [type]: [description]
    """

    passport_temp = Image.open(passport_temp_path).convert(
        'RGBA').crop((13, 13, 1330, 1873))
    passport_photo = Image.open(pasport_photo_path).convert('RGBA')
    background = Image.open(background_path).convert('RGBA')

    print('Загружен фон', background)
    width, height = passport_photo.size
    new_height = 425  # Высота
    new_width = int(new_height * width / height)
    print(new_width)
    passport_photo = passport_photo.resize(
        (new_width, new_height), Image.ANTIALIAS)
    if passport_photo.mode != 'RGBA':
        alpha_passpor_photo = Image.new('RGBA', (10, 10), 100)
        passport_photo.putalpha(alpha_passpor_photo)
    paste_mask_passport_photo = passport_photo.split()[
        3].point(lambda i: i * 90 / 100.)

    passport_temp.paste(passport_photo, (80, SH + 125),
                        mask=paste_mask_passport_photo)

    img_lis = random.choice(os.listdir('media/cfg/sing_png'))
    sing = Image.open("media/cfg/sing_png/" +
                      img_lis).resize((190, 140), Image.ANTIALIAS)
    sing_passport_photo = sing.split()[
        3].point(lambda i: i * 90 / 100.)
    passport_temp.paste(sing, (900, SH + 445), mask=sing_passport_photo)
    im = Image.open(exif_infor)
    img_exif_data = im.getexif()

    # passport_temp_crop = passport_temp.crop((13, 13, 1330, 1873))
    # passport_temp_crop = passport_temp.copy()
    # w, h = passport_temp_crop.size
    # nh = 900  # Высота
    # nw = int(nh * w / h)
    # im = passport_temp_crop.resize((nw, nh), Image.ANTIALIAS)
    im = passport_temp.copy()
    rad = 15
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    background_width, background_height = background.size
    passport_width, passport_height = im.size

    position = ((background_width // 2 - passport_width // 2),
                (background_height // 2 - passport_height // 2))
    background_new = Image.new("RGBA", (passport_width+13,
                                        passport_height+13), (60, 60, 60))
    background.paste(background_new, position)
    background.paste(im, position, mask=im)

    all_done_path = f'media/cfg/out/passport{random.randint(1000,9999)}.png'

    background.save(all_done_path, exif=img_exif_data)
    return all_done_path


def creator_archive(file):
    zipObj = ZipFile('img.zip', 'w')
    zipObj.write(file)
    zipObj.close()
    return zipObj
