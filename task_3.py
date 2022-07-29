""" 
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
"""

string = input()
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count += 1
    else:
        a = string[i]
        count = 1
    print(count, string[i])
