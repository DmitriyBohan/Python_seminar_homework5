""" 
Создайте программу для игры в ""Крестики-нолики"". 
"""


print(" Игра Крестики-нолики для двоих ")

board = list(range(1,10))

# Рисую поле , беру одномерный список с цифрами от 1 до 9, оформляю вывод в виде сетки 
def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)


#Пользователь вводит число , проверка на ввод не числа, числа вне диапозона 
def take_input(player_token):
   valid = False
   while not valid:
#Просим пользователя ввести номер квадрата. Принимаем на ввод строку
      player_answer = input("Куда поставим " + player_token+"? ")
# Пытаемся перевести введеное пользователем в int 
      try:
         player_answer = int(player_answer)
# Если не получилось то просим человека передумать вводить фигню
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
# Проверка на введение числа вне диапозона 
      if player_answer >= 1 and player_answer <= 9:
# Если пользователь ввел число в диапозоне ,но клетка уже занята ,то выводим сообщение пользователю. Если все норм , то идем дальше
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

# Создаем кортеж с выйгрышными комбинациями
def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
# Проходим циклом по списку поля и если в каждой выйгрышной комбинации проставлены одинаковые символы , то возвращаем символ ,который выйграл (Х,О) иначе Fslse
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

# функция проставляет символы X,O на поля и работает пока не один из символов не займет выйгрышные комбинации
def main(board):
# счетчик ходов
    counter = 0
    win = False
    while not win:
# когда четный ход то прописываем символ Х
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
# функцию check_win начинаем использовать после 4 хода 
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

main(board)
input("Нажмите Enter для выхода!")