from typing import Literal, get_args, Any

supported_languages = Literal["en_us", "es_mx"]

class UnsupportedLanguage(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None: pass


def error(lang: supported_languages) -> None:
    if type(lang) != str:
        raise TypeError(f'lang must be a str (not "{type(lang)}")')
    elif lang not in get_args(supported_languages):
        raise UnsupportedLanguage(f'''can only be {get_args(supported_languages)} not "{lang}"''')

error(324)