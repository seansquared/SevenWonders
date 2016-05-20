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
