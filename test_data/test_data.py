from .data_generator import TestDateGenerator


class TestDataUserAuthentication:
    USER_FOR_REGISTRATION = 'rachel.howell@reqres.in'
    PASSWORD_FOR_REGISTRATION = 'pistol'
    UNREGISTERED_USER = TestDateGenerator.email_generator()
    PASSWORD_FOR_UNREGISTERED_USER = '123456789'

    USER_DATA = {
        'email': USER_FOR_REGISTRATION,
        'password': PASSWORD_FOR_REGISTRATION
    }

    UNREGISTERED_USER_DATA = {
        'email': UNREGISTERED_USER,
        'password': PASSWORD_FOR_UNREGISTERED_USER
    }

    MISSING_REQUIRED_DATA = [({
        'email': '',
        'password': PASSWORD_FOR_REGISTRATION
    }),
        ({
            'email': USER_FOR_REGISTRATION,
            'password': ''
        }), ({
            'email': '',
            'password': ''
        })]

    MISSING_REQUIRED_DATA_ERRORS = ['Missing email or username', 'Missing password', 'Missing email or username']

    USER_WITH_INCORRECT_PASSWORD = {
        'email': USER_FOR_REGISTRATION,
        'password': PASSWORD_FOR_UNREGISTERED_USER
    }


class TestDataUsers:
    USER_NAME = 'morpheus'
    USER_JOB = 'leader'

    CREATE_USER = {
        "name": USER_NAME,
        "job": USER_JOB
    }

    MISSING_REQUIRED_DATA = [({
        'name': '',
        'job': USER_JOB
    }),
        ({
            'name': USER_NAME,
            'job': ''
        }), ({
            'name': '',
            'job': ''
        })]
