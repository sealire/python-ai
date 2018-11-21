from translate import Translator

translator = Translator(from_lang="English", to_lang="Chinese")
translation = translator.translate("I am Chinese!")
print(translation)
