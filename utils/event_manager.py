from collections import defaultdict



class EventManager:
    __instance = None

    def __new__(
            cls):
        if not EventManager.__instance:
            EventManager.__instance = object.__new__(cls)
            EventManager.__instance._callbacks = defaultdict(list)
        return EventManager.__instance


    def publish(self, event_name):
        print(f"Publishing event {event_name}")
        for callback in self._callbacks[event_name]:
            callback()

    def subscribe(self, event_name, callback):
        self._callbacks[event_name].append(callback)
