from collections import defaultdict


# collections la thu vien mac dinh cua python, can import defaultdict. defaultdict la  default dictionary giong dict
# nhung gia tri cua no luon la list. Gia tri tra ve la list, neu query 1 key ma gia tri khong ton tai thi muon tra ve
# 1 list trong thay vi tra ve gia tri null

class EventManager:
    __instance = None

    def __new__(
            cls):  # dung new thay vi init de khoi tao single ton (la object duy nhat cua he thong), duoc goi truoc init va return eventmanager
        if not EventManager.__instance:  # vi eventmanager duoc goi o nhieu cho va chi muon co 1 instant duy nhat
            EventManager.__instance = object.__new__(cls)  # __instance la 1 object cua eventmanager
            EventManager.__instance._callbacks = defaultdict(list)  # thang dau tien goi eventmanager se duoc gan vao
        return EventManager.__instance
        # instance. thang t2 duoc goi se lay tin tu instance de truyen di. instance co ttin success or fail

    def publish(self, event_name):  # cls la class
        print(f"Publishing event {event_name}")
        for callback in self._callbacks[event_name]:  # goi tung event ra
            callback()

    def subscribe(self, event_name, callback):
        self._callbacks[event_name].append(callback)
# them tung event name da subscribe vao callback
