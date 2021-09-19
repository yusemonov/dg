from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont, ImageColor
from mrz.generator.td3 import TD3CodeGenerator, dictionary
import click

# Шрифты
FONT_FOR_MAIN_INFO = ImageFont.truetype('font/sans.ttf', 36)
FONT_FOR_MRZ_INFO = ImageFont.truetype('font/cour.ttf', 50)
WIDTH = 450


class GetUserInformation():
    '''В этом классе собирается основные данные для заполнения полей в документе'''

    def __init__(self):
        '''Инициализация объектов которые входят в генерацию mrz'''
        self.document_type = click.prompt('Тип документа', default='P')
        self.document_country = click.prompt('Страна документа', default='UKR')
        self.document_surname = click.prompt('Фамилия', default='ТКАЧЕНКО')
        self.document_given_name = click.prompt('Имя', default="МАР'ЯНА")
        self.document_number = click.prompt(
            'Номер паспорта', default='XX000000')
        self.document_nationality = click.prompt(
            'Национальность', default='UKRAINE')
        self.document_birth_date = click.prompt(
            'Дата рождения', default='910824')
        self.document_genre = click.prompt('Пол', default='F')
        self.document_exp_date = click.prompt(
            'Дата окончания', default='230925')
        self.document_id_number = click.prompt(
            'Id номер документа', default='1234567890')


x = GetUserInformation()


def generate_mrz_and_return():
    ''' Функция генерирует mrz объект и передает его дальше '''
    mrz = TD3CodeGenerator(
        x.document_type,
        x.document_country,
        x.document_surname,
        x.document_given_name,
        x.document_number,
        x.document_nationality,
        x.document_birth_date,
        x.document_genre,
        x.document_exp_date,
        x.document_id_number,
        dictionary.cyrillic_ukrainian())
    return mrz


def write_main_data(mrz):
    ''' Нанесение на шаблон документа основной информации '''

    # Открываем шаблон на который необходимо нанести текст
    img = Image.open('template/ukraine_inernational.jpg')
    draw = ImageDraw.Draw(img)

    # Наносим тип документа
    draw.text((WIDTH, 1140), x.document_type,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Добавляем страну в которой выдан документ
    draw.text((623, 1140), x.document_country,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Уникальный номер документа
    draw.text((968, 1140), x.document_number,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Фамилия владельца документа
    draw.text((WIDTH, 1220), x.document_surname,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Имя влядельца документа
    draw.text((WIDTH, 1300), x.document_surname,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Добавляем гражданство владельца документа
    draw.text((WIDTH, 1376), x.document_country,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Дата рождения владельца документа
    ''' Тут нужно не забыть сделать форматирование вывода даты в формате 21 ЛИП/JUL 96'''
    draw.text((WIDTH, 1447), x.document_birth_date,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Персональный номер документа
    draw.text((980, 1455), x.document_number,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Добавляется пол владельца документа
    draw.text((WIDTH, 1522), x.document_genre,
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Город владельца документа
    draw.text((600, 1522), str(x.document_country + '/UKR'),
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Дата когда был выдан документ
    draw.text((WIDTH, 1593), "19 КВI/APR 13",
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Дата окончания действия документа
    draw.text((WIDTH, 1670), "19 КВI/APR 23",
              (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Орган который водал документ
    draw.text((980, 1593), '8099', (41, 37, 43), font=FONT_FOR_MAIN_INFO)

    # Добавляем mrz на шаюлон
    draw.text((70, 1830), str(mrz), (41, 37, 43), font=FONT_FOR_MRZ_INFO)

    img.save('tmp/pre.png')


def write_id():
    passport_number = x.document_id_number
    font = ImageFont.truetype('font/PRFW.TTF', 120)
    line_height = sum(font.getmetrics())  # в нашем случае 33 + 8 = 41

    fontimage = Image.new('L', (font.getsize(passport_number)[0], line_height))
    # И рисуем на ней белый текст
    ImageDraw.Draw(fontimage).text(
        (0, 0), passport_number, fill=255, font=font)
    fontimage = fontimage.rotate(90, resample=Image.BICUBIC, expand=True)
    orig = Image.open('tmp/pre.png')
    orig.paste((67, 67, 67), box=(30, 180), mask=fontimage)
    orig.save("out/done1.png")
    image = Image.open('out/done1.png')
    logo = Image.open('input/s.png')
    image_copy = image.copy()
    im_crop = logo.resize((round(logo.size[0]*0.7), round(logo.size[1]*0.7)))
    image_copy.paste(im_crop, (90, 1300), im_crop)
    image_copy.save('done.jpg')


if __name__ == '__main__':
    mrz = generate_mrz_and_return()
    pre_out_img = write_main_data(mrz)
    write_id()
