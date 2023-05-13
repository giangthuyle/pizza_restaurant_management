from order.order import Order
from payment.discount import Discount


class PaymentStrategy:
    def process_payment(self, order: Order, on_success, on_failure):
        pass

    def with_discounts(self, discounts: [Discount]):
        pass


class CashPaymentStrategy(PaymentStrategy):
    def __init__(self):
        super().__init__()

    def process_payment(self, order: Order, on_success, on_failure):
        print("PROCESSED")
