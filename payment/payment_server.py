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


@app.route('/callback/payment/success')
def payment_success_callback():
    app.message_queue.send((Event(name='card_payment_success'),))
    return "Payment success!"


@app.route('/callback/payment/failed')
def payment_failed_callback():
    app.message_queue.send((Event(name='card_payment_failed'),))
    return "Payment failed!"


# def stop_signal_listener(connection: Connection):
#     while True:
#         if connection.poll():
#             stop_signal = connection.recv()
#             if stop_signal == 'CLOSE':
#                 app.shutd
#


def start_payment_server(connection: Pipe):
    app.set_message_queue(connection)
    # thr = Thread(target=stop_signal_listener, args=(connection,))
    # thr.start()
    app.run(port=5000)
    # thr.join(timeout=1)


def start_payment_server_on_different_process():
    main_connection, sub_connection = Pipe()
    # Create new process for web server
    proc = Process(name='WebserverProcess', target=start_payment_server, args=(sub_connection,))

    proc.start()
    return proc, main_connection
