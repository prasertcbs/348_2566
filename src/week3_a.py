import win32com.client as wincl

def speak(s: str):
    syn = wincl.Dispatch('SAPI.SpVoice')  # use Windows SAPI (Speech API)
    syn.Rate = 0  # normal speed = 0
    syn.Volume = 100  # max volume = 100
    # print(s)
    syn.Speak(s)
    
def body_mass_index(weight_kg, height_m): # define function
    bmi = weight_kg / (height_m**2)
    return bmi

def body_mass_index2(weight_kg, height_m): # define function
    bmi = weight_kg / (height_m**2)
    print(bmi)

def bmi_status(bmi):
    if bmi >= 25:
        return "overweight"
        # print("overweight")
    elif 18.5 <= bmi < 25:
        return "normal"
        # print("normal")
    else:
        return "underweight"
        # print("underweight")

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

# print(body_mass_index(70, 1.7))
# body_mass_index2(70, 1.7)
bmi=body_mass_index(weight_kg, height_m)
print(bmi)
bmi_status_value=bmi_status(bmi)
speak(f"{bmi:.2f} You are {bmi_status_value}.")