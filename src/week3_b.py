import win32com.client as wincl

def speak(s: str):
    syn = wincl.Dispatch('SAPI.SpVoice')  # use Windows SAPI (Speech API)
    syn.Rate = 0  # normal speed = 0
    syn.Volume = 100  # max volume = 100
    # print(s)
    syn.Speak(s)
    
def body_mass_index(weight_kg, height_m): # define function
    return weight_kg / (height_m**2)

def body_mass_index2(weight_kg, height_m): # define function
    print(weight_kg / (height_m**2))

def bmi_status(bmi):
    if bmi >= 25:
        return "overweight"
    elif 18.5 <= bmi < 25:
        return "normal"
    else:
        return "underweight"


def target_weight(weight_kg, height_m):
    bmi=body_mass_index(weight_kg, height_m)
    if bmi >= 25:
        target_weight_value = 25 * (height_m**2)
    elif 18.5 <= bmi < 25:
        target_weight_value = weight_kg
    else:
        target_weight_value = 18.5 * (height_m**2)
    return target_weight_value
    
weight_kg = float(input("enter weight in kg. "))
height_m = float(input("enter height in m. "))
bmi=body_mass_index(weight_kg, height_m)
print(bmi)
# speak(f"{bmi:.2f}")
print(body_mass_index2(weight_kg, height_m))
bmi_status_value=bmi_status(bmi)
print(bmi_status_value)
speak("you are " + bmi_status_value)