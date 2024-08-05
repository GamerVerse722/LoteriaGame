from typing import Callable, Any


class classproperty:
    def __init__(self, func: Callable[[Any], Any]) -> None:
        self.func = func

    def __get__(self, instance: Any, owner: type) -> Any:
        return self.func(owner)