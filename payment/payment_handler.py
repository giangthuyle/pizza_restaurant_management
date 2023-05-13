from payment.payment_strategy import PaymentStrategy


class PaymentHandler:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
        self._success_callbacks = []
        self._failure_callbacks = []

    def _on_success(self):
        for callback in self._success_callbacks:
            callback()

    def _on_failure(self):
        pass

    def register_success_callback(self, callback):
        self._success_callbacks.append(callback)

    def register_failure_callback(self, callback):
        self._failure_callbacks.append(callback)
