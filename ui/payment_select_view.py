import tkinter as tk
import webbrowser

from payment.payment_handler import PaymentHandler
from payment.payment_strategy import CardPaymentStrategy


class PaymentSelectView(tk.Toplevel):

    def __init__(self, parent, cost: int, title='Payment Method', size='500x500+300+300'):
        super().__init__(parent)
        self._payment_handler = None
        self.title(title)
        self.geometry(size)

        self.cost = cost

        self.pay_by_cash_btn = tk.Button(master=self, text='Pay By Cash', command=self.on_select_pay_by_cash)
        self.pay_by_cash_btn.pack()

        self.pay_by_card_btn = tk.Button(master=self, text='Pay By Card', command=self.on_select_pay_by_card)
        self.pay_by_card_btn.pack()

        self.result = tk.Label()
        self.result.pack()

    def on_select_pay_by_cash(self):
        pass

    def on_select_pay_by_card(self):
        self._payment_handler = PaymentHandler(CardPaymentStrategy())
        self.open_stripe_payment_page()

    def get_payment_link(self) -> str:
        # Call to server to get a payment link
        link = 'https://buy.stripe.com/test_bIY8y37dN0Jj57a8ww'
        return link

    def show_response_message(self, message):
        self.result.config(text=message)

    def open_stripe_payment_page(self):
        link = self.get_payment_link()
        webbrowser.open(link)
        self._payment_handler.register_success_callback(callback=lambda _: self.show_response_message('Success'))
        self._payment_handler.register_failure_callback(callback=lambda _: self.show_response_message('Failed'))
