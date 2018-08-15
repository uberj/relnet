import attr
import copy

@attr.s
class DelayedInbox(object):
    station = attr.ib()
    messages = attr.ib(default=[])
    time = attr.ib(default=0)

    def get_arrived_messages(self):
        # this impl kind of sucks
        arrived = []
        for i in range(len(self.messages)):
            message = self.messages[i]
            if message[0] >= self.time:
                arrived.append(copy.copy(message))
            self.messages[i] = None

        self.messages = list(filter(lambda x: x, self.messages))
        return arrived


    def deliver(self, time_sent, time_delay, message):
        messages.append((time_delay, message))

    def advance_time(self, amount):
        self.time += amount
