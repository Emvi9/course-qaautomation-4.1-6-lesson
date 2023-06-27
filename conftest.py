import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def pytest_addoption(parser):
    parser.addoption('--language', default='en', action='store', help='Choose your language: es / fr')


@pytest.fixture(scope='class')
def browser(request):
    browser_lang = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
    return browser_lang
