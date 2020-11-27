import uuid
import datetime
import collections
import dataclasses


@dataclasses.dataclass
class Event:
    """User activity event"""
    uid: uuid.UUID = uuid.uuid1()
    timestamp: datetime.datetime = datetime.datetime.now()


class Logger:
    def __init__(self, time, threshold: int):
        self._time = time
        self._threshold = threshold
        self._log: list = []
        self._log: collections.deque
        self._counter: collections.Counter

    def new_event(self, event: Event):
        self._log.append(event)

    def get_num_active_users(self):
        pass
