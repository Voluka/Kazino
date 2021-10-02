import random

Money = 10000


def dice():
    playGame = True
    while (playGame):
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
        Money = Money - stavka
        print("Ваши деньги - ", Money)

        print("Ещё?")
        need = str(input())
        if need == "Да":
            playGame = True
        else:
            playGame = False
play = 1
while play == 1:
    print("Сыграем? Выберите игру")
    game = int(input())
    if game != 1:
        exit()
    else:
        dice()
