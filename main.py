from game.translation.translation import TranslationKey
from game.info.data import Information
# from pprint import pprint

print("------------------------------")
TranslationKey.load_lang(lang="stuff")
print(TranslationKey.get('card.1'))
print(TranslationKey.get('card.2'))
print("------------------------------")
print(Information.root_path)
print(Information.lang_path)
print(Information.__repr__())
print("------------------------------")