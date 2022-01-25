from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = browser.find_element(By.ID, "price").text
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, "book")
    # script.execute_script()
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    val_x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    calc_x = calc(val_x)
    ret_val = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(calc_x))

    # Отправляем заполненную форму
    button1 = browser.find_element(By.ID, "solve")
    button1.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()