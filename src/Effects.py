import Player
class Effects:

    def __init__(self, name, player):
        self.name = name
        self.player = player

        if (name == "Lumber Yard"):
            player.resource_count['wood'] = player.resource_count['wood'] + 1