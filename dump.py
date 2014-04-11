# class Hand:
#     def __init__(self,deck,playernum):
#         self.hand = []
#         if playernum < 4:
#             self.handsize = 5
#         else:
#             self.handsize = 4
#
#     def getHand(self):
#         for i in range(self.handsize):
#             self.hand.append(self.deck.deck.pop())
#         return self.hand
#
#     #use to get identifiers out of card objects
#     def get(self):
#         return [i.id for i in self.hand ]
#
#     def __str__(self):
#         return [i.id for i in self.hand ]





        # the zero is just the showing player
        #cardlist = []
        #targetcardlist = []
        #for card in self.players[0].hand:
        #    cardlist.append(card.color)
        #for card.color in self.players[targetPlayer].hand:
        #    targetcardlist.append(card.color)
        #matches = [x for x in targetcardlist if x in cardlist]
               #i f cards[colorindex] in self.players[targetPlayer].hand.cards.colors[colorindex]:
                #    print("its a match")

        #print(self.players[targetPlayer].hand.color[colorindex])








#initialize deck
#deck = Deck()

#create hands
#hands = []
#for i in range(playernum):
#    hands.append(Hand(deck,playernum))

#for i in hands:
#    print(i.get())

x = [[None,None]]*10
print(x)

x[3][1][0] = 4
print(x)