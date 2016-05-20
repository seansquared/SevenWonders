class Costs:

    def __init__(self, name, player):
        self.name = name
        self.player = player

        if (name == "Tree Farm"):
            player.coin_count -= 1
        if (name == "Excavation"):
            player.coin_count -= 1
        if (name == "Clay Pit"):
            player.coin_count -= 1
        if (name == "Timber Yard"):
            player.coin_count -= 1
        if (name == "Forest Cave"):
            player.coin_count -= 1
        if (name == "Mine"):
            player.coin_count -= 1
        if (name == "Saw Mill"):
            player.coin_count -= 1
        if (name == "Quarry"):
            player.coin_count -= 1
        if (name == "Brickyard"):
            player.coin_count -=1
        if (name == "Foundry"):
            player.coin_count -= 1