class Warehouse():
    x_coor = 0;
    y_coor = 0;
    no_products = 0;
    products = list();
    products_map = dict();

    def __init__(self, x_coor, y_coor, id, products):
        self.x_coor = x_coor;
        self.y_coor = y_coor;
        self.id = id
        self.products = products

        self.preprocess()

    def preprocess(self):
        for p in self.products:
            if p in selfself.products_map:
                self.products_map[p] += 1
            else:
                self.products_map[p] = 1


class AllWarehouse():
    def __init__(self):
        self.warehouses = list()
        self.product_warehouse_map = dict()

    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)
        self.process_new_warehouse()

    def process_new_warehouse(self):
        w = self.warehouses[-1]
        for (p, quantity) in w.products_map.iteritems():
            if p not in self.product_warehouse_map:
                self.product_warehouse_map = [w.id]
            else:
                self.product_warehouse_map.append(w.id)

    def find_product(self, pid):
        """Returns list of warehouse id containing the product id
        """
        return self.product_warehouse_map[pid]



