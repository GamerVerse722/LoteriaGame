from game.utils.classpropetry import classproperty
from typing import ClassVar, Any

import os

class InformationMeta(type):
    def __setattr__(cls, name: str, value: Any) -> None:
        raise AttributeError("Cannot reassign class property")

class Information(metaclass=InformationMeta):
    _root_path: ClassVar[str] = os.getcwd()
    _lang_path: ClassVar[str] = os.path.join(_root_path, "game", "resources", "lang")

    @classproperty
    def root_path(self) -> str:
        return self._root_path

    @classproperty
    def lang_path(self) -> str:
        return self._lang_path

    @classmethod
    def __repr__(cls) -> str:
        data: str = f"Information(root_path='{cls._root_path}', lang_path='{cls._lang_path}')"
        return data