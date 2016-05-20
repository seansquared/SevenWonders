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
