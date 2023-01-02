# https://pypi.python.org/pypi/pyttsx3/2.6
# Mac OS, Linux: pip install pyttsx3

def speak(s):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(s)
    engine.runAndWait()


if __name__ == '__main__':
    s = 'Life is beautiful.'
    speak(s)
