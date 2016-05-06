import eulerutils as eu

file = "p054_poker.txt"

p1hand = ['5H','5C', '6S', '7S', 'KD']
p2hand = ['2C', '3S', '8S', '8D', 'TD']
if (eu.cards.does_first_hand_win(p1hand, p2hand)):
    print("Error - Player 2 should win but Player 1 won")
else:
    print("Player 2 correctly won")

p1hand = ['5D', '8C', '9S', 'JS', 'AC']
p2hand = ['2C', '5C', '7D', '8S', 'QH']
if (eu.cards.does_first_hand_win(p1hand, p2hand)):
    print("Player 1 correctly won")
else:
    print("Error - Player 1 should win but Player 2 won")

p1hand = "2D 9C AS AH AC".split(" ")
p2hand = "3D 6D 7D TD QD".split(" ")
if (eu.cards.does_first_hand_win(p1hand, p2hand)):
    print("Error - Player 2 should win but Player 1 won")
else:
    print("Player 2 correctly won")

p1hand = "4D 6S 9H QH QC".split(" ")
p2hand = "3D 6D 7H QD QS".split(" ")
if (eu.cards.does_first_hand_win(p1hand, p2hand)):
    print("Player 1 correctly won")
else:
    print("Error - Player 1 should win but Player 2 won")

p1hand = "2H 2D 4C 4D 4S".split(" ")
p2hand = "3C 3D 3S 9S 9D".split(" ")
if (eu.cards.does_first_hand_win(p1hand, p2hand)):
    print("Player 1 correctly won")
else:
    print("Error - Player 1 should win but Player 2 won")

player1wins = 0
player2wins = 0
for line in open(file):
    line = line.strip()
    listOfCards = line.split(" ")
    p1hand = listOfCards[0:5]
    p2hand = listOfCards[5:10]
    if (eu.cards.does_first_hand_win(p1hand, p2hand)):
        player1wins += 1
    else:
        player2wins += 1

print("Player 1 wins {} of the hands, Player 2 wins {}, Total is {}".format(player1wins, player2wins, player1wins+player2wins))
