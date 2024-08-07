from game.translation.exception import UnsupportedLanguage, InvalidLanguageFile
from typing import Dict, Any, Literal, get_args, Tuple
from json.decoder import JSONDecodeError
from game.info.data import Information
import json, os

supported_languages = Literal["en_us", "es_mx"]

class TranslationKey:
    _translation: Dict[str, str] = {}
    _language: str = ""

    @classmethod
    def load_lang(cls, lang: supported_languages = "es_mx") -> None:
        cls._valid_languages(lang)
        cls._lang_file_exist(lang)
        cls._language = lang
        lang_file: str = os.path.join(Information.path.lang, f"{lang}.json")
        try:
            with open(lang_file, "r") as file:
                cls._translation = json.load(file)
        except JSONDecodeError:
            raise InvalidLanguageFile(f'Invalid JSON format in "{lang}.json"')

    @staticmethod
    def _valid_languages(lang: supported_languages) -> None:
        lang_type: Any = type(lang)
        lang_args: Tuple[Any, ...] = get_args(supported_languages)
        if lang_type != str:
            raise TypeError(f'lang must be a str (not "{lang_type}")')
        elif lang not in lang_args:
            raise UnsupportedLanguage(f'''can only be {lang_args} not "{lang}"''')

    @staticmethod
    def _lang_file_exist(lang: supported_languages) -> None:
        if f"{lang}.json" not in os.listdir(Information.path.lang):
            raise FileNotFoundError(f'Language file "{lang}.json" not found.')

    @classmethod
    def get(cls, key: str) -> str:
        return cls._translation.get(key, key)
