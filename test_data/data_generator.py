from datetime import datetime


class TestDateGenerator:
    @staticmethod
    def email_generator():
        base_part = 'TMS05'
        domain_part = 'tms.com'
        random_part = datetime.now().strftime('%d%m%Y%H%M%S')
        email = f'{base_part}{random_part}@{domain_part}'
        return email
