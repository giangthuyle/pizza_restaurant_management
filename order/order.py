from order.order_item import OrderItem


class Order:
    def __init__(self, items: [OrderItem]):
        self._items = items

    def get_total_cost(self):
        return sum(item.get_total_cost() for item in self._items)

    def to_line_items(self):
        return [item.to_line_item() for item in self._items]


