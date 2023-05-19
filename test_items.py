import time

from selenium.webdriver.common.by import By


def test_btn_add_to_basket_is_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    browser.get(link)

    time.sleep(5)

    btn_add_to_basket = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert btn_add_to_basket, 'Кнопка [Add to basket] не найдена!'