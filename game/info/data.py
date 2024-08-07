from dataclasses import dataclass
from typing import Final, Tuple, Literal, get_args
import os

@dataclass(frozen=True)
class Path:
    root: Final[str] = os.getcwd()
    resources: Final[str] = os.path.join(root, 'resources')
    lang: Final[str] = os.path.join(root, "game", "resources", "lang")


@dataclass(frozen=True)
class Information:
    path: Final[Path] = Path()