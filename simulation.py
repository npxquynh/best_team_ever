from order import *
from warehouse import *
from drone import *
from utility import *

class Simulation():
    stores = list()
    products = list()

    def __init__(self, no_rows, no_cols, no_drones, max_time, max_load):
        self.current_time = 0

        self.no_rows = no_rows
        self.no_cols = no_cols
        self.no_drones = no_drones
        self.max_time = max_time
        self.max_load = max_load

        self.all_order = AllOrder()
        self.all_warehouse = AllWarehouse()
        self.all_drone = AllDrone()

    def run(self):
        # 1 drone for all orders
        drone = self.all_drone.get_drone()
        order = self.all_order.get_next_order()

        # Load item
        for item in order.items:
            wh = self._find_item_in_warehouse(item)
            wh.remove_product(item)
            command = ('L', wh.id, item, 1) # now we only work on 1 item at a time
            new_x = wh.x_coor
            new_y = wh.y_coor
            command_time = cal_distance(drone.x_coor, drone.y_coor, new_x, new_y)
            drone.update_coor(new_x, new_y)
            drone.add_command(command, command_time)

        # Unload item
        for (item, quantity) in order.items_map.iteritems():
            command = ('D', order.id, item, quantity)
            new_x = order.x_coor
            new_y = order.y_coor
            command_time = cal_distance(drone.x_coor, drone.y_coor, new_x, new_y)
            drone.update_coor(new_x, new_y)
            drone.add_command(command, command_time)

    def _find_item_in_warehouse(self, item):
        """Returns the first warehouse
        """
        ids = self.all_warehouse.find_product(item)
        if ids:
            return self.all_warehouse[ids[0]]
        else:
            return None

    def write(self, filepath):
        total_commands = self.all_drone.no_total_command()
        with open(filepath, 'w') as output:
            output.write("%i\n" % total_commands)
            for drone in self.all_drone.drones:
                output.write(drone.get_all_commands())

    def __repr__(self):
        output = ""
        output = output + "### Simulation ###\n"
        output += str(self.no_cols) + "\n"
        output += str(self.no_drones) + "\n"

        return output