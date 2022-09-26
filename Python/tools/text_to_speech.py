import pyttsx3
engine = pyttsx3.init()
# 设置声音引擎
engine.setProperty('voice', "com.apple.speech.synthesis.voice.samantha")
text = "The earliest forms of English, collectively known as Old English"
engine.say(text)
# engine.save_to_file(text, 'test.mp3')
engine.runAndWait()
# 查看可用声音的引擎
voices = engine.getProperty('voices')
for item in voices:
    print(item)