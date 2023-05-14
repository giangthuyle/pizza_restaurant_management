from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection

from flask import Flask

from utils.event import Event


class PaymentServer(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.signal_sender = None

    def set_signal_sender(self, signal_sender: Connection):
        self.signal_sender = signal_sender

    def run_server(self, port: int):
        print("Starting payment server")
        super().run(port=port)
        print("Payment server stopped")


app = PaymentServer()  # yeu cau de chay Flask


@app.get('/callback/payment/success')  # neu duoc browser goi payment success
def payment_success_callback():
    app.signal_sender.send((Event(name='card_payment_success'),))  # tu webserver gui signal den GUI
    return "Payment success!"


@app.get('/callback/payment/failed')
def payment_failed_callback():
    app.signal_sender.send((Event(name='card_payment_failed'),))
    return "Payment failed!"


def start_payment_server(signal_sender: Connection):  # ham de run server va gan pipe
    app.set_signal_sender(signal_sender)
    app.run_server(port=5000)


def start_payment_server_on_different_process():  # ham de chay process webserver
    signal, signal_sender = Pipe()  # tao pipe
    # Create new process for web server
    web_server_process = Process(name='WebserverProcess', target=start_payment_server, args=(signal_sender,))

    web_server_process.start()
    return web_server_process, signal
