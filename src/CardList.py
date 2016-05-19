from Card import *
class CardList():

    resource_cards = []

    resource_cards.append(Card("Lumber Yard", 1, 3, "none", 0))
    resource_cards.append(Card("Stone Pit", 1, 3, "none", 0))
    resource_cards.append(Card("Clay Pool", 1, 3, "none", 0))
    resource_cards.append(Card("Ore Vein", 1, 3, "none", 0))
    resource_cards.append(Card("Clay Pit", 1, 3, "One Gold", 0))
    resource_cards.append(Card("Timber Yard", 1, 3, "One Gold", 0))
    resource_cards.append(Card("Lumber Yard", 1, 4, "none", 0))
    resource_cards.append(Card("Ore Vein", 1, 4, "none", 0))
    resource_cards.append(Card("Excavation", 1, 4, "One Gold", 0))
    resource_cards.append(Card("Stone Pit", 1, 5, "none", 0))
    resource_cards.append(Card("Clay Pool", 1, 5, "none", 0))
    resource_cards.append(Card("Forest Cave", 1, 5, "One Gold", 0))
    resource_cards.append(Card("Tree Farm", 1, 6, "One Gold", 0))
    resource_cards.append(Card("Mine", 1, 6, "One Gold", 0))
    resource_cards.append(Card("Sawmill", 2, 3, "One Gold", 0))
    resource_cards.append(Card("Quarry", 2, 3, "One Gold", 0))
    resource_cards.append(Card("Brickyard", 2, 3, "One Gold", 0))
    resource_cards.append(Card("Foundry", 2, 3, "One Gold", 0))
    resource_cards.append(Card("Sawmill", 2, 4, "One Gold", 0))
    resource_cards.append(Card("Quarry", 2, 4, "One Gold", 0))
    resource_cards.append(Card("Brickyard", 2, 4, "One Gold", 0))
    resource_cards.append(Card("Foundry", 2, 4, "One Gold", 0))

    manufactured_cards = []

    manufactured_cards.append(Card("Loom", 1, 3, "none", 0))
    manufactured_cards.append(Card("Glassworks", 1, 3, "none", 0))
    manufactured_cards.append(Card("Press", 1, 3, "none", 0))
    manufactured_cards.append(Card("Loom", 1, 6, "none", 0))
    manufactured_cards.append(Card("Glassworks", 1, 6, "none", 0))
    manufactured_cards.append(Card("Press", 1, 6, "none", 0))
    manufactured_cards.append(Card("Loom", 2, 3, "none", 0))
    manufactured_cards.append(Card("Glassworks", 2, 3, "none", 0))
    manufactured_cards.append(Card("Press", 2, 3, "none", 0))
    manufactured_cards.append(Card("Loom", 2, 5, "none", 0))
    manufactured_cards.append(Card("Glassworks", 2, 5, "none", 0))
    manufactured_cards.append(Card("Press", 2, 5, "none", 0))

    civilian_cards = []

    civilian_cards.append(Card("Baths", 1, 3, "One Stone", 0))
    civilian_cards.append(Card("Altar", 1, 3, "none", 0))
    civilian_cards.append(Card("Theater", 1, 3, "none", 0))
    civilian_cards.append(Card("Pawnshop", 1, 4, "none", 0))
    civilian_cards.append(Card("Altar", 1, 5, "none", 0))
    civilian_cards.append(Card("Theater", 1, 6, "none", 0))
    civilian_cards.append(Card("Pawnshop", 1, 7, "none", 0))
    civilian_cards.append(Card("Baths", 1, 7, "One Stone", 0))
    civilian_cards.append(Card("Aqueduct", 2, 3, "Three Stone", 0))
    civilian_cards.append(Card("Temple", 2, 3, "One Wood, One Clay, One Glass", 0))
    civilian_cards.append(Card("Statue", 2, 3, "One Wood, Two Ore", 0))
    civilian_cards.append(Card("Courthouse", 2, 3, "Two Clay, One Loom", 0))
    civilian_cards.append(Card("Courthouse", 2, 5, "Two Clay, One Loom", 0))
    civilian_cards.append(Card("Temple", 2, 6, "One Wood, One Clay, One Glass", 0))
    civilian_cards.append(Card("Aqueduct", 2, 7, "Three Stone", 0))
    civilian_cards.append(Card("Statue", 2, 7, "One Wood, Two Ore", 0))
    civilian_cards.append(Card("Pantheon", 3, 3, "Two Clay, One Ore, One Papyrus, One Loom, One Glass", 0))
    civilian_cards.append(Card("Gardens", 3, 3, "One Wood, Two Clay", 0))
    civilian_cards.append(Card("Town Hall", 3, 3, "One Glass, One Ore, Two Stone", 0))
    civilian_cards.append(Card("Palace", 3, 3, "One Glass, One Papyrus, One Loom, One Clay, One Wood, One Ore, One Stone", 0))
    civilian_cards.append(Card("Senate", 3, 3, "One Ore, One Stone, Two Wood", 0))
    civilian_cards.append(Card("Senate", 3, 5, "One Ore, One Stone, Two Wood", 0))
    civilian_cards.append(Card("Gardens", 3, 4, "One Wood, Two Clay", 0))
    civilian_cards.append(Card("Town Hall", 3, 5, "One Glass, One Ore, Two Stone", 0))
    civilian_cards.append(Card("Pantheon", 3, 6, "Two Clay, One Ore, One Papyrus, One Loom, One Glass", 0))
    civilian_cards.append(Card("Town Hall", 3, 6, "One Glass, One Ore, Two Stone", 0))
    civilian_cards.append(Card("Palace", 3, 7, "One Glass, One Papyrus, One Loom, One Clay, One Wood, One Ore, One Stone", 0))

    commerce_cards = []

    commerce_cards.append(Card("East Trading Post", 1, 3, "none", 0))
    commerce_cards.append(Card("West Trading Post", 1, 3, "none", 0))
    commerce_cards.append(Card("Marketplace", 1, 3, "none", 0))
    commerce_cards.append(Card("Tavern", 1, 4, "none", 0))
    commerce_cards.append(Card("Tavern", 1, 5, "none", 0))
    commerce_cards.append(Card("Marketplace", 1, 6, "none", 0))
    commerce_cards.append(Card("Tavern", 1, 7, "none", 0))
    commerce_cards.append(Card("East Trading Post", 1, 7, "none", 0))
    commerce_cards.append(Card("West Trading Post", 1, 7, "none", 0))
    commerce_cards.append(Card("Forum", 2, 3, "Two Clay", 0))
    commerce_cards.append(Card("Caravansery", 2, 3, "Two Wood", 0))
    commerce_cards.append(Card("Vineyard", 2, 3, "none", 0))
    commerce_cards.append(Card("Bazar", 2, 4, "none", 0))
    commerce_cards.append(Card("Caranvansery", 2, 5, "Two Wood", 0))
    commerce_cards.append(Card("Forum", 2, 6, "Two Clay", 0))
    commerce_cards.append(Card("Caravansery", 2, 6, "Two Wood", 0))
    commerce_cards.append(Card("Vineyard", 2, 6, "none", 0))
    commerce_cards.append(Card("Bazar", 2, 7, "none", 0))
    commerce_cards.append(Card("Haven", 3, 3, "One Loom, One Ore, One Wood", 0))
    commerce_cards.append(Card("Lighthouse", 3, 3, "One Glass, One Stone", 0))
    commerce_cards.append(Card("Arena", 3, 3, "One Ore, Two Stone", 0))
    commerce_cards.append(Card("Chamber of Commerce", 3, 4, "Two Clay, One Papyrus", 0))
    commerce_cards.append(Card("Haven", 3, 4, "One Loom, One Ore, One Wood", 0))
    commerce_cards.append(Card("Arena", 3, 5, "One Ore, Two Stone", 0))
    commerce_cards.append(Card("Lighthouse", 3, 6, "One Glass, One Stone", 0))
    commerce_cards.append(Card("Chamber of Commerce", 3, 6, "Two Clay, One Papyrus", 0))
    commerce_cards.append(Card("Arena", 3, 7, "One Ore, Two Stone", 0))

    military_cards = []


    military_cards.append(Card("Stockade", 1, 3, "One Wood", 0))
    military_cards.append(Card("Barracks", 1, 3, "One Ore", 0))
    military_cards.append(Card("Guard Tower", 1, 3, "One Clay", 0))
    military_cards.append(Card("Guard Tower", 1, 4, "One Clay", 0))
    military_cards.append(Card("Barracks", 1, 5, "One Ore", 0))
    military_cards.append(Card("Stockade", 1, 7, "One Wood", 0))
    military_cards.append(Card("Walls", 2, 3, "Three Stone", 0))
    military_cards.append(Card("Stables", 2, 3, "One Ore, One Clay, One Wood", 0))
    military_cards.append(Card("Archery Range", 2, 3, "Two Wood, One Ore", 0))
    military_cards.append(Card("Training Ground", 2, 4, "One Wood, Two Ore", 0))
    military_cards.append(Card("Stables", 2, 5, "One Ore, One Clay, One Wood", 0))
    military_cards.append(Card("Training Ground", 2, 6, "One Wood, Two Ore", 0))
    military_cards.append(Card("Archery Range", 2, 6, "Two Wood, One Ore", 0))
    military_cards.append(Card("Walls", 2, 7, "Three Stone", 0))
    military_cards.append(Card("Training Ground", 2, 7, "One Wood, Two Ore", 0))
    military_cards.append(Card("Fortifications", 3, 3, "One Stone, Three Ore", 0))
    military_cards.append(Card("Arsenal", 3, 3, "One Ore, Two Wood, One Loom", 0))
    military_cards.append(Card("Siege Workshop", 3, 3, "One Wood, Three Clay", 0))
    military_cards.append(Card("Circus", 3, 4, "Three Stone, One Ore", 0))
    military_cards.append(Card("Arsenal", 3, 4, "One Ore, Two Wood, One Loom", 0))
    military_cards.append(Card("Circus", 3, 5, "Three Stone, One Ore", 0))
    military_cards.append(Card("Siege Workshop", 3, 5, "One Wood, Three Clay", 0))
    military_cards.append(Card("Circus", 3, 6, "Three Stone, One Ore", 0))
    military_cards.append(Card("Arsenal", 3, 7, "One Ore, Two Wood, One Loom", 0))
    military_cards.append(Card("Fortifications", 3, 7, "One Stone, Three Ore", 0))

    science_cards = []

    science_cards.append(Card("Apothecary", 1, 3, "One Loom", 0))
    science_cards.append(Card("Workshop", 1, 3, "One Glass", 0))
    science_cards.append(Card("Scriptorium", 1, 3, "One Papyrus", 0))
    science_cards.append(Card("Scriptorium", 1, 4, "One Papyrus", 0))
    science_cards.append(Card("Apothecary", 1, 5, "One Loom", 0))
    science_cards.append(Card("Workshop", 1, 7, "One Glass", 0))
    science_cards.append(Card("Dispensary", 2, 3, "Two Ore, One Glass", 0))
    science_cards.append(Card("Laboratory", 2, 3, "Two Clay, One Papyrus", 0))
    science_cards.append(Card("Library", 2, 3, "Two Stone, One Loom", 0))
    science_cards.append(Card("School", 2, 3, "One Wood, One Papyrus", 0))
    science_cards.append(Card("Dispensary", 2, 4, "Two Ore, One Glass", 0))
    science_cards.append(Card("Laboratory", 2, 5, "Two Clay, One Papyrus", 0))
    science_cards.append(Card("Library", 2, 6, "Two Stone, One Loom", 0))
    science_cards.append(Card("School", 2, 7, "One Wood, One Papyrus", 0))
    science_cards.append(Card("Lodge", 3, 3, "Two Clay, One Loom, One Papyrus", 0))
    science_cards.append(Card("Observatory", 3, 3, "Two Ore, One Glass, One Loom", 0))
    science_cards.append(Card("University", 3, 3, "Two Wood, One Papyrus, One Glass", 0))
    science_cards.append(Card("Academy", 3, 3, "Three Stone, One Glass", 0))
    science_cards.append(Card("Study", 3, 3, "One Wood, One Papyrus, One Loom", 0))
    science_cards.append(Card("University", 3, 4, "Two Wood, One Papyrus, One Glass", 0))
    science_cards.append(Card("Study", 3, 5, "One Wood, One Papyrus, One Loom", 0))
    science_cards.append(Card("Lodge", 3, 6, "Two Clay, One Loom, One Papyrus", 0))
    science_cards.append(Card("Observatory", 3, 7, "Two Ore, One Glass, One Loom", 0))
    science_cards.append(Card("Academy", 3, 7, "Three Stone, One Glass", 0))



































