import random

num = random.randint(1, 100)

def rnd(x):
    if x > num:
        print('Слишком много, попробуйте еще раз')
    elif x < num:
        print('Слишком мало, попробуйте еще раз')
    else:
        print('Вы угадали, поздравляем!')
        return True
    return False

while True:
    x = int(input('Угадай число от 1 до 100: '))
    if rnd(x):
        break
