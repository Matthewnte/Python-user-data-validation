import random
import string


def collect_details():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    email = input('Enter email address: ')
    details = [first_name, last_name, email]
    return details


def password_generator(details):
    length = 5
    random_string = ''.join(random.choice(string.ascii_letters) for i in range(length))
    generated_password = str(details[0][:2] + details[1][-2:] + random_string)
    return generated_password
