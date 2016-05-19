from CardList import *
import random

class Deck:

    age_deck = []
    hand = []

    def __init__(self, age, player):
        self.age = age
        self.player = player

    def shuffle(age_deck, age):
        for x in range(0, len(CardList.resource_cards)):
            if (CardList.resource_cards[x].age == age):
                age_deck.append(CardList.resource_cards[x])

        for x in range(0, len(CardList.manufactured_cards)):
            if (CardList.manufactured_cards[x].age == age):
                age_deck.append(CardList.manufactured_cards[x])

        for x in range(0, len(CardList.civilian_cards)):
            if (CardList.civilian_cards[x].age == age):
                age_deck.append(CardList.civilian_cards[x])

        for x in range(0, len(CardList.commerce_cards)):
            if (CardList.commerce_cards[x].age == age):
                age_deck.append(CardList.commerce_cards[x])

        for x in range(0, len(CardList.military_cards)):
            if (CardList.military_cards[x].age == age):
                age_deck.append(CardList.military_cards[x])

        for x in range(0, len(CardList.science_cards)):
            if (CardList.science_cards[x].age == age):
                age_deck.append(CardList.science_cards[x])

        age_deck = random.shuffle(age_deck)
        for x in range(0, len(age_deck)):
            print (age_deck[x].name)


    shuffle(age_deck, 1)