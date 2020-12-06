from gtts import gTTS
import os
CATEGORIES = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","del","nothing","space"]
for i in CATEGORIES:
    m=gTTS(text=i, lang='en',slow=False)
    m.save(i + ".mp3")
print("done")