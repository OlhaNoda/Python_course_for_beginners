import random
p1, p2, p3, p4 = [], [], [], []
players = {
    1: p1,
    2: p2,
    3: p3,
    4: p4
    }
# создаем колоду карт и выбрасываем даму бубен
suits = ["Пик", "Треф", "Червей", "Бубен"]
nominals = ['6', '7', '8', '9', '10', "Валет", "Дама", "Король", "Туз"]
deck = [(nom, suit) for nom in nominals for suit in suits]
deck.remove(('Дама', 'Бубен'))

# раздаем всю колоду карт игрокам
while len(deck) != 0:
    for key in players:
        if len(deck) != 0:
            x = random.choice(deck)
            players[key].append(x)
            deck.remove(x)
        else:
            break
