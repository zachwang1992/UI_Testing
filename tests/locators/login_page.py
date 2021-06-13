from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, 'input#inputEmail')
    PASSWORD = (By.CSS_SELECTOR, 'input#inputPassword')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button.login-btn.action-btn.blue.block')
    HEADER = (By.XPATH, '//*[@id="login"]/div[4]/div[2]/h1')
    MESSAGE_BOX = (By.CSS_SELECTOR, 'p.cbox_messagebox')
    LOST_PASSWORD_LINK = (By.XPATH, '//*[@id="regular-login"]/div[3]/a')
