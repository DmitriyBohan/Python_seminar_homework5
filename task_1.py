""" 
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) (доп) Подумайте как наделить бота ""интеллектом"" 
"""



summa = 101
i=0
count=0
while summa != 0:
    if i == 0:
        print('Hodi: ')
        n = int(input())
        while n<1 or n>28:
             print('!!!!!!!!!')
             n = int(input())
        summa =summa- n
        print(f'chel vzial {n} konfet \nostalos {summa} konfet')
        i = 1
    else:
        count = summa % 29
        summa=summa-count
        print(f'komp vzial {count} konfet \nostalos {summa} konfet')
        i=0
if i==1:
    print('chel viigral')
else:
    print('II viigral')
