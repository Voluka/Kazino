import random

Money = 10000


def dice():
    global Money
    print("Ваши деньги - ", Money)
    print("Введите ставку - ")
    stavka = int(input())
    print("Ваша ставка - ", stavka)
    print('Выбирай число')
    x = int(input("Твой выбор- "))
    y = random.randint(1, 6)
    print(y)
    if x == y:
        print('Вы угадали')
        win = stavka * 6
        Money = Money + win
        print("Ваши деньги - ", Money)
    else:
        print('Вы не угадали')
    defeat = Money - stavka
    
play = 1
while play == 1:
    print("Сыграем? Выберите игру")
    game = int(input())
    if game != 1:
        exit()
    else:
        dice()
    print("сыграем ещё?")
    play = int(input())