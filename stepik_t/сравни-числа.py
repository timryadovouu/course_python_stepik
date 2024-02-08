import random
iskomoe = random.randint(1,100)
print('-----Добро пожаловать в угадайку!-----')
print('-----СПОЙЛЕР-----', iskomoe, '-----СПОЙЛЕР-----')
left, right, flag = 1, 100, False
middle = (left+right) // 2
def is_valid(num):
   if num.isdigit() and 1 <= int(num) <= 100:
       return True
   else:
       return False
def compare_numbers():
    while True:
        n = input('Введи число мой хороший: ')
        if is_valid(n) == True:
            n = int(n)
            if n < iskomoe:
                print('Надо ввести больше')
            if n > iskomoe:
                print('Ваше ввести меньше')
            if n == iskomoe:
                print('Угадали')
                break
        else:
            print('Ты дегрот сука что ли?')
compare_numbers()
