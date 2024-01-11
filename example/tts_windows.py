# %%
# pip install pypiwin32

"""Text-to-Speech demo
doc: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ms723602(v=vs.85)
"""
import win32com.client as wincl

def speak(s: str):
    syn = wincl.Dispatch('SAPI.SpVoice')  # use Windows SAPI (Speech API)
    syn.Rate = 0  # normal speed = 0
    syn.Volume = 100  # max volume = 100
    # print(s)
    syn.Speak(s)

# %%
if __name__ == '__main__':
    s = 'Coding is beautiful'
    # s = 'สวัสดีครับ'
    # s = 'Happy Chinese New Year!!'
    # s = input('enter text: ')
    speak(s)
