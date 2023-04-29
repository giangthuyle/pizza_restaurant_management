import random
import tkinter as tk

from ui.payment_select_view import PaymentSelectView


class MainView(tk.Tk):

    def __init__(self, title='Restaurant', size='500x300+200+200'):
        super().__init__()
        self.title(title)

        self.geometry(size)

        self._total_cost = random.Random().randint(200, 1000)
        self.total_pay = tk.Label(text=f'Total: ${self._total_cost}')
        self.total_pay.pack()

        self.confirm_order_btn = tk.Button(master=self, text='Confirm Order', command=self.on_confirm_order)
        self.confirm_order_btn.pack()

    def on_confirm_order(self):
        payment_select = PaymentSelectView(parent=self, cost=self._total_cost)
        payment_select.grab_set()