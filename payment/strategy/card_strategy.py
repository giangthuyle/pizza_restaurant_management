from order.order import Order
from payment.payment_server import app
from payment.strategy.payment_strategy import PaymentStrategy
import stripe
import webbrowser

from utils.event_manager import EventManager


class CardPaymentStrategy(PaymentStrategy):
    def __init__(self):
        super().__init__()
        self._api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

    def process_payment(self, order: Order, on_success=None, on_failure=None):
        stripe.api_key = self._api_key
        # Generate a payment link
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=order.to_line_items(),
            mode='payment',
            success_url='http://127.0.0.1:5000/callback/payment/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:5000/callback/payment/failed?session_id={CHECKOUT_SESSION_ID}',
        )
        self._register_card_payment_callback(on_success, on_failure)
        # Open the link in browser
        webbrowser.open(session.url)

    def _register_card_payment_callback(self, on_success, on_failure):
        if on_success:
            EventManager().subscribe('card_payment_success', on_success)
        if on_failure:
            EventManager().subscribe('card_payment_failed', on_failure)
