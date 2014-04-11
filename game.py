from random import shuffle



#class Singleton(object):
#  _instances = {}
#  def __new__(class_, *args, **kwargs):
#    if class_ not in class_._instances:
#        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
#    return class_._instances[class_]
colors = ['Red','White','Blue','Green','Yellow']
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
        #[[[None, None]], [[None, None]], [[None, None]]
        # clues[card#][0 or 1 for color or number][value]
        self.clues = [[[None,None]]]*5



class State:
    def __init__(self):
        self.tokens = 8
        self.bombs = 3
        self.playerturn = 0
        self.deck = Deck()

        self.playerarray = []
        for i in range(5):
            self.playerarray.append(Player(self.deck))


        #I finally figured it out how to print the 2 letter card identifiers
        #this will print the first card of the first player, its random
        print(self.playerarray[0].hand[3][1])


    def tellColor(self,target,color):
        for n in self.playerarray[target].hand:
            print(n[1].color)
            if =



stato = State()
stato.tellColor(2,3)



