from random import shuffle

playernum = 4

#class Singleton(object):
#  _instances = {}
#  def __new__(class_, *args, **kwargs):
#    if class_ not in class_._instances:
#        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
#    return class_._instances[class_]


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

    def __str__(self):
        for i in self.deck:
            print(i)


class Hand:
    def __init__(self,deck,playernum):
        self.hand = []
        if playernum < 4:
            handsize = 5
        else:
            handsize = 4

        for i in range(handsize):
            self.hand.append(deck.deck.pop())


    #use to get identifiers out of card objects
    def get(self):
        return [i.id for i in self.hand ]

    def __str__(self):
        return [i.id for i in self.hand ]



class Player:
    def __init__(self,id,hand):
        self.id = id
        self.hand = hand
        self.ident = { self.id : self.hand}



class State:
    def __init__(self,playernum):
        self.tokens = 8
        self.bombs = 3
        self.playerturn = 0
        self.players = {}
        self.deck = Deck()
        for r in range(playernum):
            #Player(r, Hand(self.deck,playernum))
            #print(Player.ident[r])
            self.players[r] = Hand(self.deck,playernum)
            print(self.players[r].get())

    #Players get color list from their hand which contains cards which contains colors
    def giveColor(self,targetPlayer,colorindex):
        for cards in self.players[0]:
            if

        #print(self.players[targetPlayer].hand.color[colorindex])








#initialize deck
#deck = Deck()

#create hands
#hands = []
#for i in range(playernum):
#    hands.append(Hand(deck,playernum))

#for i in hands:
#    print(i.get())

State(playernum).giveColor(3,1)

