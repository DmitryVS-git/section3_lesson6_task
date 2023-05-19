import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    # По умолчанию сделал значение у default не None, чтобы при работе с Firefox и без передачи параметра --language в
    # терминале не было ошибки. Сделал это на всякий случай.
    parser.addoption('--language', action='store', default='fr'
                     , help='Choose language: ru, en, etc...')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_lang = request.config.getoption("language")

    if browser_name == "chrome":
        options = ChromeOptions()
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_lang)
        browser = webdriver.Firefox(options=options)
        print("\nstart firefox browser for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
