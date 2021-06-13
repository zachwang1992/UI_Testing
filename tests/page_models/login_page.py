from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators.login_page import LoginPageLocators
from tests.page_models.base_page import BasePage
TIMEOUT = 6


class LoginPage(BasePage):
    @property
    def url(self):
        return super().url + 'login/'

    @property
    def header(self):
        return WebDriverWait(self.browser, TIMEOUT).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.HEADER))

    @property
    def message_box(self):
        return WebDriverWait(self.browser, TIMEOUT).until(
            expected_conditions.presence_of_element_located(LoginPageLocators.MESSAGE_BOX))

    @property
    def username_field(self):
        return self.browser.find_element(*LoginPageLocators.EMAIL)

    @property
    def password_field(self):
        return self.browser.find_element(*LoginPageLocators.PASSWORD)

    def fill_email_and_password(self, email, password):
        self.username_field.send_keys(email)
        self.password_field.send_keys(password)

    def click_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def press_enter_key_to_login(self):
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Keys.ENTER)

    def click_lost_password_link(self):
        self.browser.find_element(*LoginPageLocators.LOST_PASSWORD_LINK).click()