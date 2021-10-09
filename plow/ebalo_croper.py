from PIL import Image
import face_recognition
import random
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def crop_face(img):
    image = face_recognition.load_image_file(img)
    face_loca = face_recognition.face_locations(image)

    for face_location in face_loca:
        top, right, bottom, left = face_location
        face_image = image[top-65:bottom+30, left-20:right+30]
        pil_image = Image.fromarray(face_image)
        pil_image.save(BASE_DIR / 'media/cfg/tmp/one_time.png')
