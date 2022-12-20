import string
import random


class UtilitiesHelper():

    def __init__(self):
        pass

    def generate_random_email_and_password(self, domain=None, email_prefix=None):
        """

        domain:
        email_prefix: email preposition
        return: Generates random email and password
        """

        if not domain:
            domain = 'example.com'

        if not email_prefix:
            email_prefix = 'test_user'

        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

        email = email_prefix + '_' + random_string + '@' + domain

        password_length = 20
        password_string = ''.join(random.choices(string.ascii_lowercase, k=password_length))

        random_info = {'email': email, 'password': password_string}

        return random_info

    def generate_random_first_and_last_name(self, f_name_pre='test f', l_name_pre='test l'):
        """

        f_name_pre: First name preposition
        l_name_pre: Last name preposition
        return: Generates random first and last name
        """

        random_f_name = f_name_pre + ''.join(random.choices(string.ascii_lowercase, k=7))
        random_l_name = l_name_pre + ''.join(random.choices(string.ascii_lowercase, k=7))

        return {'f_name': random_f_name, 'l_name': random_l_name}

    def generate_random_coupon_code(self, suffix=None, length=10):
        """

        suffix:Suffix that will be use in the beginning
        length: Expected length of the word
        return: Generates random coupon code
        """
        random_code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if suffix:
            code = suffix + random_code
        else:

            code = random_code
        return code

    def generate_random_lorem_ipsum(self, length=20):
        """

        return: Generates random text
        """
        random_lorem = ''.join(random.choices(string.ascii_lowercase, k=length))
        return random_lorem

    def select_valid_random_email(self):
        """

        return: A random valid email from the list below
        """
        valid_emails = ["george.bluth@reqres.in", "janet.weaver@reqres.in", "emma.wong@reqres.in", "eve.holt@reqres.in",
                        "charles.morris@reqres.in", "tracey.ramos@reqres.in"
                        ]
        random_email = random.choice(valid_emails)

        return random_email

    def generate_random_type(self):
        """

        return: A random type from the list below
        """
        types_list = ["Python", "Java", "C", "C++", "JavaScript", "SQL", "PHP", "GO", "R",
                      "Matlab", "Swift", "Ruby", "Scala"]
        random_type = random.choice(types_list)

        return random_type
