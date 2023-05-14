from order.order import Order


class PaymentStrategy:
    def process_payment(self, order: Order, on_success, on_failure):
        pass
