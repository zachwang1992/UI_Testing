import os


class CredentialsUtility:
    @staticmethod
    def get_account_email():

        email = os.environ.get('EMAIL')

        if not email:
            raise Exception("The account credentials 'EMAIL' must be in env variable")
        else:
            return email

    @staticmethod
    def get_account_password():

        password = os.environ.get('PASSWORD')

        if not password:
            raise Exception("The account credentials 'PASSWORD' must be in env variable")
        else:
            return password
