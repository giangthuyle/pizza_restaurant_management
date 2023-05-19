from order.order_item import OrderItem


class Order:
    def __init__(self, items: [OrderItem]):
        self._items_of_order = items

    def get_total_order_cost(self):  #cost of total items
        return sum(item.get_total_item_cost() for item in self._items_of_order)

    def to_line_items(self):  #each item in order follow stripe format
        return [item.to_stripe_format() for item in self._items_of_order]
