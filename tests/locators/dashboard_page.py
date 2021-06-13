from selenium.webdriver.common.by import By


class DashboardPageLocators:
    PROFILE_MENU = (By.CSS_SELECTOR, 'a.admin-dropdown.profile')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'button.action-btn.block.blue')