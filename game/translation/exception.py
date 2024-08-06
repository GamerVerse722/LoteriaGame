from typing import Any

class UnsupportedLanguage(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None: pass

class InvalidLanguageFile(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None: pass