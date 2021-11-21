'''3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']'''

sample_data = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
temp_data = []
for i in range(len(sample_data)):
    len(sample_data[i])
    if len(sample_data[i]) != 0:
        temp_data.append(sample_data[i])
print(temp_data)
