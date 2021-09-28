from enum import Enum
from typing import Iterator


class ProxyIter:
    def __init__(self):
        self.counter = 1
        self.limit = 10  # каждый 10й запрос *

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.limit:
            self.counter = 1
            return self.RouteType.SERVER  # * отправляем на сервер
        else:
            self.counter += 1
            return self.RouteType.CDN  # остальные на cdn

    class RouteType(Enum):
        CDN = 0
        SERVER = 1

