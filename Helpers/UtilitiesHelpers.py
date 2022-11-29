import string
import random

class UtilitiesHelper():

    def __init__(self):
        pass

    def generate_random_email_and_password(self, domain=None, email_prefix=None):
        """

        :param domain:
        :param email_prefix: email preposition
        :return: Generates random email and password
        """

        if not domain:
            domain = 'example.com'

        if not email_prefix:
            email_prefix='testuser'

        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

        email = email_prefix + '_' + random_string + '@' + domain

        password_length = 20
        password_string = ''.join(random.choices(string.ascii_lowercase, k=password_length))

        random_info = {'email': email, 'password': password_string}
        #print("Random email and password {}".format(random_info))
        return random_info


    def generate_random_first_and_last_name(self, f_name_pre = 'test f', l_name_pre = 'test l'):
        """

        :param f_name_pre: First name preposition
        :param l_name_pre: Last name preposition
        :return: Generates random first and last name
        """

        random_f_name = f_name_pre + ''.join(random.choices(string.ascii_lowercase, k=7))
        random_l_name = l_name_pre + ''.join(random.choices(string.ascii_lowercase, k=7))

        return {'f_name': random_f_name, 'l_name': random_l_name}


    def generate_random_coupon_code(self, sufix=None, length=10):
        """

        :param sufix:
        :param length:
        :return: Generates random coupon code
        """
        random_code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if sufix:
            code = sufix + random_code
        else:

            code = random_code
        return code

    def generate_random_lorem_ipsum(self, length=20):
        """

        :return: Generates random text
        """
        random_lorem = ''.join(random.choices(string.ascii_lowercase, k=length))
        return random_lorem
