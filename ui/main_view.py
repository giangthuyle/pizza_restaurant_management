import tkinter as tk

from ui.payment_select_view import PaymentSelectView
from utils.event_manager import EventManager


class MainView(tk.Tk):

    def __init__(self, title='Restaurant', size='500x300+200+200'):
        super().__init__()
        self.title(title)

        self.geometry(size)

        self._total_cost = 55
        self.total_pay = tk.Label(text=f'Total: ${self._total_cost}')
        self.total_pay.pack()

        self.confirm_order_btn = tk.Button(master=self, text='Confirm Order', command=self.on_confirm_order)
        self.confirm_order_btn.pack()

        self.reset_btn = tk.Button(master=self, text='Back', command=self.on_reset_click)

        self.register_callbacks()

    def handle_success_callback(self):  # la 1 method (function cua class nay), de goi attributes trong class
        self.total_pay.configure(text='Payment Success')
        self.confirm_order_btn.pack_forget()  # an nut confirm order di

    def handle_failed_callback(self):
        self.total_pay.configure(text='Payment Failed')
        self.confirm_order_btn.pack_forget()
        self.reset_btn.pack()  # hien nut reset

    def register_callbacks(self):  # neu event manager tra ve success hay fail thi hien text
        EventManager().subscribe('card_payment_success', self.handle_success_callback)
        EventManager().subscribe('card_payment_failed', self.handle_failed_callback)

    # khi subscribe nhan event success/fail thi goi function self. handle_success/fail_callback
    def on_confirm_order(self):  # khi an confirm order thi show ra man hinh paymentselect
        payment_select = PaymentSelectView(parent=self)
        payment_select.grab_set()  # dung grab set vi la window

    def on_reset_click(self):
        self.total_pay.configure(
            text=f'Total: ${self._total_cost}')  # configure de show lai total cost sau khi da an di o tren)
        self.confirm_order_btn.pack()
        self.reset_btn.pack_forget()  # an nut reset
