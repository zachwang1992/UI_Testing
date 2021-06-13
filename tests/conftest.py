import logging as logger
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


@pytest.fixture(scope='function')
def browser():
    logger.info('starting browser...')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://wave-trial.getbynder.com/login/')
    yield browser
    logger.info('quiting browser...')
    browser.quit()
