import tkinter as tk

from order.order import Order
from order.order_item import OrderItem
from payment.strategy.card_strategy import CardPaymentStrategy


class PaymentSelectView(tk.Toplevel):

    def __init__(self, parent, title='Making Online Payment', size='500x500+300+300'):
        super().__init__(parent)
        self._payment_strategy = None
        self.title(title)
        self.geometry(size)

        self.pay_by_card_btn = tk.Button(master=self, text='Pay By Card', command=self.on_select_pay_by_card)
        self.pay_by_card_btn.pack()

    def on_select_pay_by_card(self):
        self._payment_strategy = CardPaymentStrategy()
        mocked_order = Order(
            items=[
                OrderItem(item_name='Pizza', item_quantity=2, item_price=2000),
                OrderItem(item_name='Spagetti', item_quantity=1, item_price=1500),
            ]
        )
        self._payment_strategy.process_payment(mocked_order)
        self.destroy()
