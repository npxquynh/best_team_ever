class Order():
    def __init__(self, x_coor, y_coor, no_items, items):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.no_items = no_items
        self.items = items

class AllOrder():
    def __init__(self):
        self.orders = list()
        self.no_orders = 0
        self.active_order_ids = list()
        self.no_active_orders = 0

    def add_order(self, order):
        self.orders.append(order)
        self.no_orders = len(self.orders)

        self.no_active_orders += 1
        self.active_order_ids.append(self.no_orders - 1)

    def remove_order_id(self, id):
        self.active_order_ids.remove(id)
        self.no_active_orders = len(self.active_order_ids)


