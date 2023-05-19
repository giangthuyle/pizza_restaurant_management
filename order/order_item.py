class OrderItem:
    def __init__(self, item_name: str, item_price: int, item_quantity: int):
        self._item_name = item_name
        self._item_price = item_price
        self._item_quantity = item_quantity

    def get_total_item_cost(self):  # cost of each item
        return self._item_price * self._item_quantity

    def to_stripe_format(self):  # show info of item
        return {
            'price_data': {
                'currency': 'aud',
                'product_data': {
                    'name': self._item_name,

                },
                'unit_amount': self._item_price,
            },
            'quantity': self._item_quantity,
        }
