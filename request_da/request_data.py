import json
from plow.plow import *
from pathlib import Path
from source_podliver.settings import MEDIA_ROOT
import random


def get_data_from_form(date_form):
    typedoc = date_form['typedoc']
    country = date_form['country']
    surname = date_form['surname']
    given_name = date_form['given_name']
    passport_number = date_form['passport_number']
    genre = date_form['genre']
    nationality = date_form['nationality']
    birth_date = date_form['birth_date']
    personal_number = date_form['personal_number']
    locations = date_form['locations']
    id_number = date_form['id_number']
    data_start = date_form['data_start']
    exp_date = date_form['exp_date']
    issuing = date_form['issuing']
    pasport_photo_path = date_form['photo_doc']
    mrz = TD3CodeGenerator(typedoc, country, surname, given_name, passport_number, nationality, birth_date, genre, exp_date, id_number,
                           dictionary.cyrillic_ukrainian())
    print(mrz)
    save_after_main_data_p = write_main_data(
        mrz, 'media/cfg/tmp/after_m_data.png', typedoc,  country,  id_number,  surname,  given_name,  genre,  birth_date)
    print(save_after_main_data_p)

    write_id_path = write_id(save_after_main_data_p, passport_number)
    print(write_id_path)
    print(pasport_photo_path)
    done_image = f'media/cfg/out/passport{random.randint(1000,9999)}.png'
    all_done = paste_photo(write_id_path, pasport_photo_path,
                           'media/cfg/template/holo.png', done_image)
    print(done_image)
    return done_image
