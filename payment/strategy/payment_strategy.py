from order.order import Order


class PaymentStrategy:
    def process_payment(self, order: Order, on_success, on_failure):
        pass


class CashPaymentStrategy(PaymentStrategy):
    def __init__(self):
        super().__init__()

    def process_payment(self, order: Order, on_success, on_failure):
        print("PROCESSED")
