class Order():
    def __init__(self, x_coor, y_coor, id, no_items, items):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.id = id
        self.no_items = no_items
        self.items = items

        self.preprocess()

    def preprocess(self):
        self.items_map = dict()
        for item in self.items:
            if item in self.items_map:
                self.items_map[item] += 1
            else:
                self.items_map[item] = 0

    def __repr__(self):
        outstr = "%s\n" % self.items
        return outstr


class AllOrder():
    def __init__(self):
        self.orders = list()
        self.no_orders = 0
        self.active_order_ids = list()
        self.no_queueing_orders = 0
        self.no_processing_orders = 0

    def add_order(self, order):
        self.orders.append(order)
        self.no_orders = len(self.orders)

        self.no_queueing_orders += 1
        self.active_order_ids.append(self.no_orders - 1)

    def get_next_order(self):
        """Returns the order to process next
        """
        if (self.active_order_ids):
            id = self.active_order_ids.pop()
            self.no_processing_orders += 1
            self.no_queueing_orders -= 1
            return self.orders[id]
        else:
            return None

    def remove_order_id(self, id):
        self.active_order_ids.remove(id)
        self.no_queueing_orders = len(self.active_order_ids)


