from gtts import gTTS
import os
from googletrans import Translator
texts=input("Enter text:")
translator=Translator()
print(type(texts))
test_to_translate_hindi=translator.translate(texts,src='en',dest='hi')
test_to_translate_kannada=translator.translate(texts,src='en',dest='kn')
test_to_translate_telugu=translator.translate(texts,src='en',dest='te')
test_to_translate_tamil=translator.translate(texts,src='en',dest='ta')
test_to_translate_marathi=translator.translate(texts,src='en',dest='mr')
obj_hindi=gTTS(text=test_to_translate_hindi.text,lang='hi',slow=False)
obj_hindi.save("speech_hindi.mp3")
obj_kannada=gTTS(text=test_to_translate_kannada.text,lang='kn',slow=False)
obj_kannada.save("speech_kannada.mp3")
obj_telugu=gTTS(text=test_to_translate_telugu.text,lang='te',slow=False)
obj_telugu.save("speech_telugu.mp3")
obj_tamil=gTTS(text=test_to_translate_tamil.text,lang='ta',slow=False)
obj_tamil.save("speech_tamil.mp3")
obj_marathi=gTTS(text=test_to_translate_marathi.text,lang='hi',slow=False)
obj_marathi.save("speech_marathi.mp3")