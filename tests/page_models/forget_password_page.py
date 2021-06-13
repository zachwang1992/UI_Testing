from tests.locators.forget_password_page import ForgetPasswordPageLocators
from tests.page_models.base_page import BasePage


class ForgetPasswordPage(BasePage):
    @property
    def url(self):
        return super().url + 'user/forgotPassword/'

    @property
    def email_field(self):
        return self.browser.find_element(*ForgetPasswordPageLocators.EMAIL)

    @property
    def send_instructions_button(self):
        return self.browser.find_element(*ForgetPasswordPageLocators.SEND_INSTRUCTIONS_BUTTON)