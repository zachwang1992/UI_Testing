from selenium.webdriver.common.by import By


class ForgetPasswordPageLocators:
    EMAIL = (By.CSS_SELECTOR, 'input#forgotPassword')
    SEND_INSTRUCTIONS_BUTTON = (By.CSS_SELECTOR, 'button#sendPassword.action-btn.blue')