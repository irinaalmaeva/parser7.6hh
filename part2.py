# Преобразование данных
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