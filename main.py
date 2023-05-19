from multiprocessing.connection import Connection
from threading import Thread

from payment.payment_server import start_payment_server_on_different_process
from ui.main_view import MainView
from utils.event import Event
from utils.event_manager import EventManager


def event_distribute(signal: Connection):
    while True:
        if signal.poll():  #check for events
            try:
                (event, *args) = signal.recv()
                if isinstance(event, Event):
                    EventManager().publish(event.name)  # if have event -> call event manager and publish event name
            except EOFError as _:
                return


if __name__ == '__main__':
    app = MainView(title='Yummy Pizza Restaurant')

    payment_webserver_process, signal = start_payment_server_on_different_process()
    event_distribute_thread = Thread(target=event_distribute, args=(signal,))
    event_distribute_thread.start()
    app.mainloop()

    payment_webserver_process.terminate()
    payment_webserver_process.join()
    event_distribute_thread.join()
