import attr
from typing import Tuple, List

RXStationName = str
RXStationTimeClaim = int


@attr.s  # type: ignore
class Message(object):
    sending_station_name = attr.ib(type=str)  # type: ignore
    time_sent = attr.ib(type=int)  # type: ignore
    rx_claims = attr.ib(  # type: ignore
            type=List[Tuple[RXStationName, RXStationTimeClaim]])
