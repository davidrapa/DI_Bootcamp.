from translate import Translator

def translate_french_to_english(french_words):
    translator = Translator(to_lang="en")
    translations = {}

    for word in french_words:
        translation = translator.translate(word)
        translations[word] = translation

    return translations
