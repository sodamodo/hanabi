from random import shuffle

class Card:
    colors = ['Red','White','Blue','Green','Yellow']
    numbers = [1,2,3,4,5]
    frequenices = [3,2,2,2,1]

    def __init__(self,col,num):
        self.color = self.colors[col]
        self.number = self.numbers[num]

    def __str__(self):
        return self.color[0] + str(self.number)




class Deck:
    def __init__(self):
        self.deck = []
        for color in range(len(Card.colors)):
            for number in range(len(Card.numbers)):
                for count in range(Card.frequencies[number]):
                    self.deck.append(Card(color,number))

    def __str__(self):
        for i in self.deck:
            print(i)


class Hand:
    def __init__(self,deck):
        self.hand = []
        for i in range(5):
            self.hand.append(deck.deck.pop())

    def __str__(self):
        for i in self.hand:
            print(i)





# testDeck = Deck()
# testHand = Hand(testDeck)


print("Hi!")