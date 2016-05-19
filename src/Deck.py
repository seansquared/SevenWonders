from CardList import *
import random

class Deck:

    def __init__(self, age, player):
        self.age = age
        self.player = player

    def shuffle(age, player):
        age_deck = []
        for x in range(0, (len(CardList.resource_cards))):
            if ((CardList.resource_cards[x].age == age) and (CardList.resource_cards[x].player <= player)):
                age_deck.append(CardList.resource_cards[x])

        for x in range(0, (len(CardList.manufactured_cards))):
            if ((CardList.manufactured_cards[x].age == age) and (CardList.manufactured_cards[x].player <= player)):
                age_deck.append(CardList.manufactured_cards[x])

        for x in range(0, (len(CardList.civilian_cards))):
            if ((CardList.civilian_cards[x].age == age) and (CardList.civilian_cards[x].player <= player)):
                age_deck.append(CardList.civilian_cards[x])

        for x in range(0, (len(CardList.commerce_cards))):
            if ((CardList.commerce_cards[x].age == age) and (CardList.commerce_cards[x].player <= player)):
                age_deck.append(CardList.commerce_cards[x])

        for x in range(0, (len(CardList.military_cards))):
            if ((CardList.military_cards[x].age == age) and (CardList.military_cards[x].player <= player)):
                age_deck.append(CardList.military_cards[x])

        for x in range(0, (len(CardList.science_cards))):
            if ((CardList.science_cards[x].age == age) and (CardList.science_cards[x].player <= player)):
                age_deck.append(CardList.science_cards[x])

        age_deck = random.sample(age_deck, len(age_deck))
        age_deck = random.sample(age_deck, len(age_deck))
        age_deck = random.sample(age_deck, len(age_deck))

        return age_deck

    def hand(deck, player):
        hand = []
        for x in range(0, 7):
            hand.append(deck[x])
        return hand

    ay = shuffle(1, 3)
    handrwef = hand(ay, 7)
    for x in range(0,7):
        del ay[x]
    handrwef = hand(ay, 7)
    for x in range(0, 7):
        del ay[x]
    handrwef = hand(ay, 7)
    for x in range(0, 7):
        del ay[x]
    print(handrwef)
    print(ay)

