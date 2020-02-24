import playsound
from gtts import gTTS
import os
q1 = '''Which of the following are applications of Machine learning ?
Natural Language processing
Robotics
Weather prediction
All of the above
'''
q2 = '''What is the size of INT datatype in C++ ?
1 bytes
2 bytes
4 bytes
8 bytes
'''
language = 'en'
  
myobj1 = gTTS(text=q1, lang=language, slow=False)
myobj2 = gTTS(text=q2, lang=language, slow=False)

myobj1.save("q1.mp3") 
myobj2.save("q2.mp3")
playsound.playsound('q1.mp3', True)