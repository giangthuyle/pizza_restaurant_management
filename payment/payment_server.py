from multiprocessing import Process, Pipe

from flask import Flask

from utils.event import Event


class PaymentServer(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_queue = None

    def set_message_queue(self, message_queue: Pipe):
        self.message_queue = message_queue

    def run(self, *args, **kwargs):
        print("Starting payment server")
        super().run(*args, **kwargs)
        print("Payment server stopped")


app = PaymentServer(__name__)


@app.get('/callback/payment/success')
def payment_success_callback():
    app.message_queue.send((Event(name='card_payment_success'),))
    return "Payment success!"


@app.get('/callback/payment/failed')
def payment_failed_callback():
    app.message_queue.send((Event(name='card_payment_failed'),))
    return "Payment failed!"


def start_payment_server(connection: Pipe):
    app.set_message_queue(connection)
    app.run(port=5000)


def start_payment_server_on_different_process():
    main_connection, sub_connection = Pipe()
    # Create new process for web server
    proc = Process(name='WebserverProcess', target=start_payment_server, args=(sub_connection,))

    proc.start()
    return proc, main_connection
