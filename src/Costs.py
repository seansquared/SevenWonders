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
            player.coin_count -= 1
        if (name == "Foundry"):
            player.coin_count -= 1

        if (name == "Baths"):
            player.civilian_count += 3
        if (name == "Altar"):
            player.civilian_count += 2
        if (name == "Theater"):
            player.civilian_count += 2
        if (name == "Aqueduct"):
            player.civilian_count += 5
        if (name == "Temple"):
            player.civilian_count += 3
        if (name == "Statue"):
            player.civilian_count += 4
        if (name == "Pantheon"):
            player.civilian_count += 7
        if (name == "Gardens"):
            player.civilian_count += 5
        if (name == "Town Hall"):
            player.civilian_count += 6
        if (name == "Palace"):
            player.civilian_count += 8