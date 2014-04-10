from random import shuffle



#class Singleton(object):
#  _instances = {}
#  def __new__(class_, *args, **kwargs):
#    if class_ not in class_._instances:
#        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
#    return class_._instances[class_]

playernum = 4

if playernum < 4:
    handsize = 5
else:
    handsize = 4


class Card:
    colors = ['Red','White','Blue','Green','Yellow']
    numbers = [1,2,3,4,5]
    frequenices = [3,2,2,2,1]

    def __init__(self,col,num):
        self.color = self.colors[col]
        self.number = self.numbers[num]
        self.id = self.color[0] + str(self.number)

    def __str__(self):
        return self.color[0] + str(self.number)


class Deck:
    def __init__(self):
        self.deck = []
        for color in range(len(Card.colors)):
            for number in range(len(Card.numbers)):
                for count in range(Card.frequenices[number]):
                    self.deck.append(Card(color,number))
        shuffle(self.deck)

    def firstDeal(self):
        hand = []
        for i in range(handsize):
            hand.append(self.deck.pop())

        return [(i, j) for i, j in enumerate(hand)]


    def __str__(self):
        for i in self.deck:
            print(i)

class Player:
    def __init__(self,deck):
        self.hand = deck.firstDeal()


class State:
    def __init__(self):
        self.tokens = 8
        self.bombs = 3
        self.playerturn = 0
        self.deck = Deck()
        self.tehplaya = Player(self.deck)

        # So I can't print out card representations yet without doing this, but Ill come back to that later
        print(self.tehplaya.hand[0][1])

State()



