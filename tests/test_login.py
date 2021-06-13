import logging as logger

import pytest

from tests.page_models.dashboard_page import DashboardPage
from tests.page_models.forget_password_page import ForgetPasswordPage
from tests.page_models.login_page import LoginPage
from tests.utilities.page_utilities import AccountCredentials, Messages, Url


class TestLoginFeature:
    def test_login_and_log_out_successfully(self, browser):
        """
        The function tests that a user can log in and log out successfully using valid username and password.
        :param browser: fixture
        :return: None
        """
        login_page = LoginPage(browser)
        logger.info('filling username and password...')
        login_page.fill_email_and_password(AccountCredentials.EMAIL, AccountCredentials.PASSWORD)
        logger.info('logging in...')
        login_page.click_login()
        dashboard_page = DashboardPage(browser)
        assert browser.current_url == dashboard_page.url
        logger.info('in dashboard page...')

        logger.info('logging out...')
        dashboard_page.hover_to_profile_menu()
        dashboard_page.click_logout()
        login_page = LoginPage(browser)
        assert browser.current_url == login_page.url
        assert login_page.message_box.text == Messages.LOGOUT_MESSAGE
        logger.info('back to login page...')

    @pytest.mark.parametrize('email, password', [(AccountCredentials.WRONG_EMAIL, AccountCredentials.PASSWORD),
                                                 (AccountCredentials.EMAIL, AccountCredentials.WRONG_PASSWORD),
                                                 (AccountCredentials.WRONG_EMAIL, AccountCredentials.WRONG_PASSWORD)])
    def test_login_with_non_existing_username_or_password(self, browser, email, password):
        """
        The function tests that a user can not log in using a non-existing username or password.
        :param browser: fixture
        :param email: pytest parameter, email used to log in
        :param password: pytest parameter, password used to log in
        :return: Optional[Any]
        """
        login_page = LoginPage(browser)
        logger.info('filling non-existing username or password...')
        login_page.fill_email_and_password(email, password)
        logger.info('logging in...')
        login_page.click_login()

        if browser.current_url == Url.SECURITY_PAGE_URL:
            logger.info('switching to security page...')
        else:
            assert browser.current_url in login_page.url
            assert login_page.message_box.text == Messages.INCORRECT_LOGIN_MESSAGE
            logger.info('incorrect username or password...')

    @pytest.mark.parametrize('email, password', [(AccountCredentials.EMAIL, AccountCredentials.EMPTY_PASSWORD),
                                                 (AccountCredentials.WRONG_EMAIL, AccountCredentials.EMPTY_PASSWORD),
                                                 (AccountCredentials.EMPTY_EMAIL, AccountCredentials.EMPTY_PASSWORD)])
    def test_login_with_empty_password(self, browser, email, password):
        """
        The function tests that a user can not log in using empty password.
        :param browser: fixture
        :param email: pytest parameter, email used to log in
        :param password: pytest parameter, password used to log in
        :return: Optional[Any]
        """
        login_page = LoginPage(browser)
        logger.info('filling empty password...')
        login_page.fill_email_and_password(email, password)
        logger.info('clicking button to log in...')
        login_page.click_login()

        if browser.current_url == Url.SECURITY_PAGE_URL:
            logger.info('switching to security page...')
        else:
            assert browser.current_url in login_page.url
            assert login_page.message_box.text == Messages.NO_PASSWORD_MESSAGE
            logger.info('password is not provided...')

    @pytest.mark.parametrize('email, password', [(AccountCredentials.EMPTY_EMAIL, AccountCredentials.PASSWORD),
                                                 (AccountCredentials.EMPTY_EMAIL, AccountCredentials.WRONG_PASSWORD)])
    def test_login_with_empty_username(self, browser, email, password):
        """
        The function tests that a user can not log in using empty password.
        :param browser: fixture
        :param email: pytest parameter, email used to log in
        :param password: pytest parameter, password used to log in
        :return: Optional[Any]
        """
        login_page = LoginPage(browser)
        logger.info('filling empty username...')
        login_page.fill_email_and_password(email, password)
        logger.info('logging in...')
        login_page.click_login()

        if browser.current_url == Url.SECURITY_PAGE_URL:
            logger.info('switching to security page...')
        else:
            assert browser.current_url in login_page.url
            assert login_page.message_box.text == Messages.NO_USERNAME_MESSAGE
            logger.info('username is not provided...')

    def test_password_is_displayed_marked(self, browser):
        """
        The function tests that password field in login page is marked.
        :param browser: fixture
        :return: None
        """
        login_page = LoginPage(browser)
        logger.info('checking type of username and password field...')
        assert login_page.username_field.get_attribute('type') == 'text'
        assert login_page.password_field.get_attribute('type') == 'password'

    def test_enter_key_can_be_used_to_log_in(self, browser):
        """
        The function tests that a user can press enter key to log in.
        :param browser: fixture
        :return: None
        """
        login_page = LoginPage(browser)
        logger.info('filling username and password...')
        login_page.fill_email_and_password(AccountCredentials.EMAIL, AccountCredentials.PASSWORD)
        logger.info('pressing enter key to log in...')
        login_page.press_enter_key_to_login()
        dashboard_page = DashboardPage(browser)
        assert browser.current_url == dashboard_page.url
        logger.info('in dashboard page...')

    def test_go_back_after_login(self, browser):
        """
        The function tests that user is still on dash board page by clicking back button in browser after logging in to
        dashboard page.
        :param browser: fixture
        :return: None
        """
        login_page = LoginPage(browser)
        logger.info('filling username and password...')
        login_page.fill_email_and_password(AccountCredentials.EMAIL, AccountCredentials.PASSWORD)
        logger.info('logging in...')
        login_page.click_login()
        dashboard_page = DashboardPage(browser)
        assert browser.current_url == dashboard_page.url
        logger.info('in dashboard page...')

        logger.info('clicking back button of browser...')
        browser.back()
        assert browser.current_url.lower() in dashboard_page.url
        logger.info('still in dashboard page...')

    def test_go_back_after_logout(self, browser):
        """
        The function tests that user is still on login page by clicking back button in browser after logging out to
        login page.
        :param browser: fixture
        :return: None
        """
        login_page = LoginPage(browser)
        logger.info('filling username and password...')
        login_page.fill_email_and_password(AccountCredentials.EMAIL, AccountCredentials.PASSWORD)
        logger.info('logging in...')
        login_page.click_login()
        dashboard_page = DashboardPage(browser)
        assert browser.current_url == dashboard_page.url
        logger.info('in dashboard page...')

        logger.info('logging out...')
        dashboard_page.hover_to_profile_menu()
        dashboard_page.click_logout()
        login_page = LoginPage(browser)
        assert browser.current_url == login_page.url
        assert login_page.message_box.text == Messages.LOGOUT_MESSAGE
        logger.info('back to login page...')

        logger.info('pressing back button of browser...')
        browser.back()
        assert login_page.url in browser.current_url
        logger.info('still in login page...')

    def test_lost_password(self, browser):
        """
        The function tests that user can go to forget password page by clicking lost password link.
        :param browser: fixture
        :return: None
        """
        login_page = LoginPage(browser)
        logger.info('clicking lost password link...')
        login_page.click_lost_password_link()
        forget_password_page = ForgetPasswordPage(browser)
        assert browser.current_url == forget_password_page.url
        logger.info('in forget password page...')
        assert forget_password_page.email_field.is_displayed()
        assert forget_password_page.send_instructions_button.is_enabled()
