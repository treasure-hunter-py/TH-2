'''1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.'''
   
test_list_input = ['aaaa','bbbb','cccc','dddd','eeee','ffff','gggg','jjjj', 123, 222222222, 555555]
up_task = ''
for i in test_list_input:
    up_task += str(i)
print(up_task)
