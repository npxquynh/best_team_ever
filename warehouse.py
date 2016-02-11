class Warehouse():
    x_coor = 0;
    y_coor = 0;
    no_products = 0;
    products = list();
    products_map = dict();

    def __init__(self, x_coor, y_coor, products):
        self.x_coor = x_coor;
        self.y_coor = y_coor;
        self.products = products

        self.preprocess()

    def preprocess(self):
        for p in self.products:
            if p in self.products_map:
                self.products_map[p] += 1
            else:
                self.products_map[p] = 1


class AllWarehouse():
    def __init__(self):
        self.warehouses = list()

    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)

