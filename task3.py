from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

URL = 'https://betandyou-227625.top/pl/bonus/rules'
driver.get(URL)

WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'bonuses-app-list__item'))
) # чекаємо поки драйвер підгрузить сторінку і знайде елементи бонусів

bonus_items = driver.find_elements(By.CLASS_NAME, 'bonuses-app-list__item')
for item in bonus_items:
    name_element = item.find_element(By.CLASS_NAME, 'template-compiler.bonuses-bonus-tile-name__compile')
    name = name_element.get_attribute('innerHTML').strip()
    print(name)

driver.quit()
