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
        for (index, p) in enumerate(self.products):
            self.products_map[index] = p
            if (index == 258):
                print self.products_map[index]

    def find_product(self, pid):
        """Returns the remaining quantity
        Otherwise, returns -1
        """
        # print self.products_map[258]
        if self.products_map[pid] != 0:
            return 1
        else:
            return -1

    def remove_product(self, pid):
        if pid in self.products_map:
            if self.products_map[pid] > 1:
                self.products_map[pid] -= 1
            elif self.products_map[pid] == 1:
                self.products_map.pop(pid)
            else:
                print "ERROR remove_product for warehouse %i, pid = %i" % (self.id, pid)
        else:
            print "ERROR remove_product for warehouse %i, pid = %i" % (self.id, pid)


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
                self.product_warehouse_map[p] = [w.id]
            else:
                self.product_warehouse_map[p].append(w.id)

    def find_product(self, pid):
        """Returns list of warehouse id containing the product id
        """
        wids = list()

        for w in self.warehouses:
            if (pid == 258):
                print "258 %s" % w.find_product(pid)
            if (w.find_product(pid) != -1):
                wids.append(w.id)

        print wids

        return wids

    def __getitem__(self, i):
        return self.warehouses[i]



