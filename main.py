from simulation import *
from warehouse import *
from utility import *

input_filepath = './busy_day.in'

if __name__ == '__main__':

    with open(input_filepath) as f:
        first_line = f.readline().strip().split(' ')

        no_rows = int(first_line[0])
        no_cols = int(first_line[1])
        no_drones = int(first_line[2])
        max_time = int(first_line[3])
        max_load = int(first_line[4])

        sim = Simulation(no_rows, no_cols, no_drones, max_time, max_load)

        # Processing the products
        no_products = int(f.readline().strip());
        product_weight_vec = [0 for i in range(no_products)]
        weights = f.readline().strip().split(' ')
        for (index, w) in enumerate(weights):
            product_weight_vec[index] = int(w)

        # Processing the warehouse
        all_warehouse = AllWarehouse() # contains all warehouses
        no_warehouses = int(f.readline().strip());

        for i in range(no_warehouses):
            coordinates = [int(p) for p in f.readline().strip().split(' ')];
            x_coor = int(coordinates[0]);
            y_coor = int(coordinates[1])

            products = f.readline().strip().split(' ');
            products = [int(p) for p in products]

            w = Warehouse(x_coor, y_coor, i, products)
            all_warehouse.add_warehouse(w)

        # Processing the orders
        all_order = AllOrder()
        no_orders = int(f.readline().strip())

        for i in range(no_orders):
            coordinates = [int(c) for c in f.readline().strip().split(' ')]
            x_coor = coordinates[0]
            y_coor = coordinates[1]

            no_items = int(f.readline().strip());

            items = f.readline().strip().split(' ');
            items = [int(p) for p in products]

            o = Order(x_coor, y_coor, i, no_items, items)
            all_order.add_order(o)

        # Creating all the drones
        all_drone = AllDrone(max_time)
        drone_x_coor = all_warehouse[0].x_coor
        drone_y_coor = all_warehouse[0].y_coor

        for i in range(no_drones):
            d = Drone(drone_x_coor, drone_y_coor, i, max_load)
            all_drone.add_drone(d)

        sim.all_order = all_order
        sim.all_warehouse = all_warehouse
        sim.all_drone = all_drone

        print sim
        sim.run()
        sim.write("busy_day.out")

        print cal_distance(2, 1, 5, 3)




