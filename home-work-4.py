'''4. Написати скрипт, який об'єднає три словника в новий. Початкові словники не повинні змінитись. Дані можна "захардкодити".
        Sample Dictionary :
        dict_1 = {1:10, 2:20}
        dict_2 = {3:30, 4:40}
        dict_3 = {5:50, 6:60}
        Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}
dict_4 = {}

dict_4.update(dict_1)
dict_4.update(dict_2)
dict_4.update(dict_3)
dict_4.update(dict_4)
print('Result : {0}'.format(dict_4))
