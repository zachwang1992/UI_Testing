from selenium.webdriver import ActionChains

from tests.locators.dashboard_page import DashboardPageLocators
from tests.page_models.base_page import BasePage


class DashboardPage(BasePage):
    @property
    def url(self):
        return super().url + 'account/dashboard/'

    @property
    def profile_menu(self):
        return self.browser.find_element(*DashboardPageLocators.PROFILE_MENU)

    def hover_to_profile_menu(self):
        actions = ActionChains(self.browser)
        actions.move_to_element(self.profile_menu)
        actions.perform()

    def click_logout(self):
        self.browser.find_element(*DashboardPageLocators.LOGOUT_BUTTON).click()
