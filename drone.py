class Drone():
    def __init__(self, x_coor, y_coor, id, max_load):
        self.load = 0
        self.current_time = 0
        self.commands = list() # of tuple of 1 string and 3 integers (L, 0, 0, 0)
        self.commands_time = list()

        self.x_coor = x_coor
        self.y_coor = y_coor
        self.id = id
        self.max_load = max_load

    def add_command(self, command, command_time):
        self.commands.append(command)
        self.commands_time.append(command_time)
        self.current_time += command_time


class AllDrone():
    def __init__(self):
        self.drones = list()

    def add_drone(self, drone):
        self.drones.append(drone)

    def get_drone(self):
        # Simplest case, always return drone 0
        return self.drones[0]