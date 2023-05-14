from multiprocessing.connection import Connection
from threading import Thread

from payment.payment_server import start_payment_server_on_different_process
from ui.main_view import MainView
from utils.event import Event
from utils.event_manager import EventManager


def event_distribute(signal: Connection):
    while True:
        if signal.poll():  # kiem tra xem co event nao gui den khong
            try:
                (event, *args) = signal.recv()  # doc event
                if isinstance(event, Event):
                    EventManager().publish(event.name)  # neu co event thi goi event manager va publish name
            except EOFError as _:  # khi server shutdown co eoferror thi thoat khoi vong lap while
                return


if __name__ == '__main__':
    app = MainView(title='Yummy Pizza Restaurant')

    payment_webserver_process, signal = start_payment_server_on_different_process()
    event_distribute_thread = Thread(target=event_distribute, args=(signal,))
    # thread va process giong nhau: duoc sinh ra de chay chuong trinh song song(multiprocessing)
    # diem khac nhau: 2 process ko chia se chung vung nho, thread chia se chung vung nho
    # 1 process co nhieu thread, cac process ko chia se chung vung nho
    # thread chay song song, se lien tuc kiem tra signal xem co event gi moi ko
    event_distribute_thread.start()  # lien tuc kiem tra xem signal co event gi moi ko, neu co thi doc va thong bao cho
    # tat ca process cua GUI
    app.mainloop()

    payment_webserver_process.terminate()
    payment_webserver_process.join()
    event_distribute_thread.join()
