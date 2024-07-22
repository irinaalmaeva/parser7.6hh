import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

url = "https://hh.ru/vacancies/finansovyy_analitik"

# Запуск браузера(открытие сайта)
driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')

parsed_data = []
for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CLASS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk ')
        company = vacancy.find_element(By.CLASS_SELECTOR, 'spain.company-info-text--vgvZouLtf8jwBmaD1xgp')
        salary = vacancy.find_element(By.CLASS_SELECTOR, 'spain.compensation-text--kTJ0_rp54B2vNeZ3CTt2')
        link = vacancy.find_element(By.CLASS_SELECTOR, 'serp-item__title').get_attribute('href')

    parsed_data.append([title, company, link])
