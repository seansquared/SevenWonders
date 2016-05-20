class Effects:

    def __init__(self, name, player):
        self.name = name
        self.player = player

        if (name == "Lumber Yard"):
            player.resource_count['wood'] += 1
        if (name == "Stone Pit"):
            player.resource_count['stone'] += 1
        if (name == "Clay Pool"):
            player.resource_count['clay'] += 1
        if (name == "Ore Vein"):
            player.resource_count['ore'] += 1
        """TODO Tree Farm, Excavation, Clay Pit, Timber Yard, Forest Cave, Mine"""
        if (name == "Saw Mill"):
            player.resource_count['wood'] += 2
        if (name == "Quarry"):
            player.resource_count['stone'] += 2
        if (name == "Brickyard"):
            player.resource_count['clay'] += 2
        if (name == "Foundry"):
            player.resource_count['ore'] += 2
        if (name == "Loom"):
            player.manufactured_count['loom'] += 1
        if (name == "Glassworks"):
            player.manufactured_count['glass'] += 1
        if (name == "Press"):
            player.manufactured_count['papyrus'] += 1

        if (name == "Pawnshop"):
            player.civilian_count += 3
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

        if (name == "Tavern"):
            player.coin_count += 5
