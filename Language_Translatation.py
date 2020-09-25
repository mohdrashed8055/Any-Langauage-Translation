# pip install googletrans

# Import library for translator
from googletrans import Translator

translator = Translator()

print(translator.translate('안녕하세요.'))
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>

print(translator.translate('안녕하세요.', dest='ja'))
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>

print(translator.translate('veritas lux mea', src='la'))
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

# Hindi
print(translator.translate("सहकारी समिति पर वार्षिक वित्त अधिनियम की पहली अनुसूची के भाग 1 का पैरा ख के अधीन निर्धारित दरों पर कर लगाया जाता है। "))

# Marathi
print(translator.translate("देव काेणाला दर्शन देताे याचे उदाहरण या कथेतून आपणास पहायला मिळेल."))




# pip install translate

from translate import Translator
translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
print(translation)

translator= Translator(to_lang="Hindi")
translation = translator.translate("Good Morning!")
print(translation)

# B/w any two languages
from translate import Translator
translator= Translator(from_lang="Hindi",to_lang="Marathi")
translation = translator.translate("सुप्रभात!")
print(translation)














