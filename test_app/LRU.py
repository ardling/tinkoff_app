from typing import Any, Hashable
from collections import OrderedDict


class LRU:
    def __init__(self, size: int):
        self._size = size
        self._cache: OrderedDict = OrderedDict()

    def __getitem__(self, key: Hashable) -> Any:
        value = self._cache[key]
        self._cache.move_to_end(key)
        return value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if len(self._cache) == self._size:
            self._cache.popitem()
        self._cache[key] = value