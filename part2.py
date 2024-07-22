# Получение информации с сайта
import requests
from bs4 import BeautifulSoup

url = "https://"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")
data = []

for row in rows:
    cols = row.find_all("td")
    cleaned_cols = [col.text.strip() for col in cols]  # очистка от лишних пробелов
    data.append(cleaned_cols)

    print(data)
# Преобразование данных ив числа
data = [
    ['100', '200', '300'],
    ['400', '500', '600']
   ]
# С сайта мы получаем именно списки.
numbers = []

for row in data:
    for text in row:
     number = int(text)
     numbers.append(number)

print(numbers)


# Фильтрация данных
# data =[
#      [100, 200, 300],
#      [400, 500, 600],
#      [150, 160, 180]
#  ]
# list = []
# for row in data:
#     for item in row:
#         if item > 190:
#            list.append(item)
# print(list)