from tests.utilities.credentials_utilities import CredentialsUtility
from tests.utilities.generic_utilities import generate_a_random_password


class AccountCredentials:
    EMAIL = CredentialsUtility.get_account_email()
    PASSWORD = CredentialsUtility.get_account_password()
    WRONG_EMAIL = 'zach1992@gmail.com'
    EMPTY_EMAIL = ''
    WRONG_PASSWORD = generate_a_random_password()
    EMPTY_PASSWORD = ''


class Messages:
    LOGOUT_MESSAGE = 'You have successfully logged out.'
    INCORRECT_LOGIN_MESSAGE = 'You have entered an incorrect username or password.'
    NO_PASSWORD_MESSAGE = 'Please enter your password.'
    NO_USERNAME_MESSAGE = 'Please enter your Username.'


class Url:
    SECURITY_PAGE_URL = 'https://wave-trial.getbynder.com/verify/'
