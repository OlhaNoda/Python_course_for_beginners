# Карточная игра "Ведьма"
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
noms = ['6', '7', '8', '9', '10', "Валет", "Дама", "Король", "Туз"]
deck = [(nom, suit) for nom in noms for suit in suits]
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


def print_players_decks():
    for num in players:
        print(num, players[num])


print('Раздали карты игрокам')
print_players_decks()

# игроки выбрасывают пары карт с одинаковым номиналом
for p in players:
    p_deck = players[p]
    i = 0
    k = 0
    while i < len(p_deck) - 1:
        k = i + 1
        while k < len(p_deck):
            if p_deck[i][0] == p_deck[k][0]:
                del p_deck[k]
                del p_deck[i]
                k = i + 1
            else:
                k += 1
        i += 1

print('Карты игроков после сброса парных карт')
print_players_decks()









