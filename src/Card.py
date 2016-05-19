
class Card():

    name = ""
    cost = ""
    state = 0
    age = 0
    player = 0

    def __init__(self, name, age, player, cost, state):
        name = name.self
        cost = cost.self
        state = state.self
        age = age.self
        player = player.self

    def name(self, name):
        return name

    def age(self, age):
        return age

    def player(self, player):
        return player

    def cost(self, cost):
        return cost

    def state(self, state):
        return state


###make this a Pyfunction to generate GCODE initial conditions
file = open("geecode.txt", "w")
file.write(";layer_height = 0.3\n")
file.write(";perimeters = 4\n")
file.write(";top_solid_layers = 2\n")
file.write(";bottom_solid_laters = 3\n")
file.write(";fill_density = 1\n")