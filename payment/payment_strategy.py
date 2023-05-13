from payment.discount import Discount


class PaymentStrategy:
    def process_payment(self):
        pass

    def with_discounts(self, discounts: [Discount]):
        pass


class CashPaymentStrategy(PaymentStrategy):
    def __init__(self):
        super().__init__()

    def process_payment(self):
        print("PROCESSED")


class CardPaymentStrategy(PaymentStrategy):
    def __init__(self):
        super().__init__()
