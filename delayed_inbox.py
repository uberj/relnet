import attr
from typing import List, Tuple
from types import Message
from station import Station


@attr.s
class DelayedInbox(object):
    station = attr.ib(type=Station)
    messages = attr.ib(default=[], type=List[Tuple[int, Message]])
    time = attr.ib(default=0)

    def get_arrived_messages(self) -> List[Message]:
        arrived = []
        idxs_to_remove = []
        for idx, (delivery_time, message) in enumerate(self.messages):
            if delivery_time >= self.time:
                idxs_to_remove.append(idx)
                arrived.append(message)

        for idx in reversed(idxs_to_remove):
            self.messages.pop(idx)

        return arrived

    def deliver(self, time_sent: int, time_delay: int, message: Message):
        self.messages.append((time_delay, message))

    def advance_time(self, amount):
        self.time += amount
