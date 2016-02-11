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

    def update_coor(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor

    def get_all_commands(self):
        """Returns the string to write to file
        """
        output = ""
        for com in self.commands:
            output = output + "%s %s\n" % (self.id, " ".join([str(s) for s in com]))

        return output

class AllDrone():
    def __init__(self):
        self.drones = list()

    def add_drone(self, drone):
        self.drones.append(drone)

    def get_drone(self):
        # Simplest case, always return drone 0
        return self.drones[0]

    def no_total_command(self):
        s = 0
        for drone in self.drones:
            s += len(drone.commands)
        return s

    def __getitem__(self, i):
        return self.drones[i]