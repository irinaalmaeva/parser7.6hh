import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "https://hh.ru/vacancies/finansovyy_analitik"

# Запуск браузера(открытие сайта)
driver.get(url)

wait = WebDriverWait(driver, 10)

try:
    vacancies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')))
except Exception as e:
    print("Произошла ошибка при загрузке вакансий:", str(e))
    driver.quit()
    exit()

parsed_data = []
for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--vgvZouLtf8jwBmaD1xgp').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')



    except Exception as e:
        print('Произошла ошибка при парсинге данных:', str(e))
        continue

    parsed_data.append([title, company, salary, link])

    driver.quit()
    with open ("hh.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(["Название вакансии", "Компания", "Зарплата", "Ссылка на вакансию"])
        writer.writerows(parsed_data)


