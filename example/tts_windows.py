# %%
# pip install pypiwin32
import win32com.client as wincl

def speak(s):
    syn = wincl.Dispatch('SAPI.SpVoice')  # use Windows SAPI (Speech API)
    syn.Rate = 0  # normal speed = 0
    syn.Volume = 100  # max volume = 100
    # print(s)
    syn.Speak(s)

# %%
s = 'Hello my students'
speak(s)

# %%
