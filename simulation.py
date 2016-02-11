from order import *
from warehouse import *

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

    def __repr__(self):
        output = ""
        output = output + "### Simulation ###\n"
        output += str(self.no_cols)

        return output