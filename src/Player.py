class Player(object):

    def __init__(self):
        self.coin_count = 0
        self.military_win = 0
        self.military_loss = 0
        self.commerce_cost = {'l_wood': 0, 'l_stone': 0, 'l_clay': 0, 'l_ore': 0, 'l_loom': 0, 'l_glass': 0, 'l_papyrus': 0,
                              'r_wood': 0, 'r_stone': 0, 'r_clay': 0, 'r_ore': 0, 'r_loom': 0, 'r_glass': 0, 'r_papyrus': 0}

        self.resource_count = {'wood': 0, 'stone': 0, 'clay': 0, 'ore': 0}
        self.resource_temp = {}
        self.manufactured_count = {'loom': 0, 'glass': 0, 'papyrus': 0}
        self.manufactured_temp = {}
        self.science_count = {'sc1': 0, 'sc2': 0, 'sc3': 0}
        self.civilian_count = 0
        self.military_count = 0

        self.resource_play = []
        self.manufactured_play = []
        self.science_play = []
        self.civilian_play = []
        self.military_play = []




