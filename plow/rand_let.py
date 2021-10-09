
import random


def generator_unique_id():
    a = chr(random.randint(ord('A'), ord('Z')))
    b = chr(random.randint(ord('A'), ord('Z')))
    num = str(random.randint(10000, 99999))
    done = str(a+b + ' № ' + num)
    return done


def issuing_d(b_date):
    yy = str(b_date[0:2])
    mm = str(b_date[2:4])
    dd = str(b_date[4:6])
    rand_y = random.randint(12, 21)
    rand_d = random.randint(10, 29)
    random_b_date = f'{rand_y}{mm}{rand_d}'
    return random_b_date


def exp_date_r(issusin):
    yy = str(issusin[0:2])
    mm = str(issusin[2:4])
    dd = str(issusin[4:6])
    y_exp = int(yy) + 10
    rand_d = random.randint(10, 29)
    date_exp = f'{y_exp}{mm}{rand_d}'
    return date_exp
