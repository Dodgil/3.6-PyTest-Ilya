import time
from selenium.common.exceptions import TimeoutException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector('#add_to_basket_form [type="submit"]')
        return True
    except:
        return False




def test_checking_the_resence_button(browser):
    browser.get(link)
    # Проверка наличия кнопки
    time.sleep(30) # Задержка для проверки надписи.
    assert is_element_present(browser)==True, "Кнопка не найдена"
    