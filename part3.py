import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

url = "https://hh.ru/vacancies/finansovyy_menedzher"

# Запуск браузера(открытие сайта)
driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')




    except:
        print('Произошла ошибка при парсинге данных:')
        continue

    parsed_data.append([title, company, salary, link])

# Вызов driver.quit() должен быть за пределами цикла for, чтобы закрыть браузер только после того, как все данные будут собраны.

driver.quit()
# Запись данных в CSV файл
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(["Название вакансии", "Компания", "Зарплата", "Ссылка на вакансию"])
        writer.writerows(parsed_data)


print('Данные успешно записаны в CSV файл')