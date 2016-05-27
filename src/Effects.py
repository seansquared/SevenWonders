class Effects:

    """Create class that asks which resource player wants every turn, stores all commerce and double resources in temp"""

    def __init__(self, name, player):
        self.name = name
        self.player = player

        #resources
        if (name == "Lumber Yard"):
            player.resource_count['wood'] += 1
        if (name == "Stone Pit"):
            player.resource_count['stone'] += 1
        if (name == "Clay Pool"):
            player.resource_count['clay'] += 1
        if (name == "Ore Vein"):
            player.resource_count['ore'] += 1
        if (name == "Tree Farm"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
        if (name == "Excavation"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
        if (name == "Clay Pit"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
        if (name == "Timber Yard"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
        if (name == "Forest Cave"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
        if (name == "Mine"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
        if (name == "Saw Mill"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
                player.resource_count['wood'] += 2
        if (name == "Quarry"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
                player.resource_count['stone'] += 2
        if (name == "Brickyard"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
                player.resource_count['clay'] += 2
        if (name == "Foundry"):
            if (player.coin_count >= 1):
                player.coin_count -= 1
                player.resource_count['ore'] += 2
        if (name == "Loom"):
            player.manufactured_count['loom'] += 1
        if (name == "Glassworks"):
            player.manufactured_count['glass'] += 1
        if (name == "Press"):
            player.manufactured_count['papyrus'] += 1

        #civic structures
        if (name == "Pawnshop"):
            player.civilian_count += 3
        if (name == "Baths"):
            if (player.resource_count['stone'] + player.resource_temp['stone'] >= 1):
                player.civilian_count += 3
        if (name == "Altar"):
            player.civilian_count += 2
        if (name == "Theater"):
            player.civilian_count += 2
        if (name == "Aqueduct"):
            if (player.resource_count['stone'] + player.resource_temp['stone'] >= 3):
                player.civilian_count += 5
        if (name == "Temple"):
            if ((player.resource_count['wood'] + player.resource_temp['wood'] >= 1) and (player.resource_count['clay'] + player.resource_temp['clay'] >= 1) and (player.resource_count['glass'] + player.resource_temp['glass'] >= 1)):
                player.civilian_count += 3
        if (name == "Statue"):
            if ((player.resource_count['wood'] + player.resource_temp['wood'] >= 1) and (player.resource_count['ore'] + player.resource_temp['ore'] >= 2)):
                player.civilian_count += 4
        if (name == "Pantheon"):
            if ((player.resource_count['clay'] + player.resource_temp['clay'] >= 2) and (player.resource_count['ore'] + player.resource_temp['ore'] >= 1) and (player.resource_count['papyrus'] + player.resource_temp['papyrus'] >= 1) and (player.resource_count['loom'] + player.resource_temp['loom'] >= 1) and (player.resource_count['glass'] + player.resource_temp['glass'] >= 1)):
                player.civilian_count += 7
        if (name == "Gardens"):
            if ((player.resource_count['wood'] + player.resource_temp['wood'] >= 1) and (player.resource_count['clay'] + player.resource_temp['clay'] >= 2)):
                player.civilian_count += 5
        if (name == "Town Hall"):
            if ((player.resource_count['glass'] + player.resource_temp['glass'] >= 1) and (player.resource_count['ore'] + player.resource_temp['ore'] >= 1) and (player.resource_count['stone'] + player.resource_temp['stone'] >= 2)):
                player.civilian_count += 6
        if (name == "Palace"):
            if ((player.resource_count['clay'] + player.resource_temp['clay'] >= 1) and (player.resource_count['ore'] + player.resource_temp['ore'] >= 1) and (player.resource_count['papyrus'] + player.resource_temp['papyrus'] >= 1) and (player.resource_count['loom'] + player.resource_temp['loom'] >= 1) and (player.resource_count['glass'] + player.resource_temp['glass'] >= 1) and (player.resource_count['stone'] + player.resource_temp['stone'] >= 1) and (player.resource_count['wood'] + player.resource_temp['wood'] >= 1)):
                player.civilian_count += 8
        if (name == "Courthouse"):
            if ((player.resource_count['clay'] + player.resource_temp['clay'] >= 2) and (player.resource_count['loom'] + player.resource_temp['loom'] >= 1)):
                player.civilian_count += 4
        if (name == "Senate"):
            if ((player.resource_count['ore'] + player.resource_temp['ore'] >= 1) and (player.resource_count['stone'] + player.resource_temp['stone'] >= 1) and (player.resource_count['wood'] + player.resource_temp['wood'] >= 2)):
                player.civilian_count += 6

        if (name == "Tavern"):
            player.coin_count += 5
