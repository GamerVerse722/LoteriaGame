from game.translation.translation import TranslationKey
from game.info.data import Information

print("------------------------------")
TranslationKey.load_lang(lang="es_mx")
print(TranslationKey.get('card.1'))
print(TranslationKey.get('card.2'))
print("------------------------------")
print(Information.path.root)
print(Information.path.lang)
print("------------------------------")