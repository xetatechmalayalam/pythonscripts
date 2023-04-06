#import libraries
from gtts import gTTS
from playsound import playsound
import os

#input text
text = "നമസ്കാരം. ഇത് ഒരു ടെക്സ്റ്റ് ടു സ്പീച് സ്ക്രിപ്റ്റാണ്."

#convert text
tts = gTTS(text, lang='ml')

#save to mp3
tts.save("speech.mp3")

#play the result
playsound('speech.mp3')

