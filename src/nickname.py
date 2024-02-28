# %%
nickname = input("enter your nickname: ")
# upper(nickname[0])
# nickname.len()
if len(nickname) > 0:
    first_char = nickname[0].upper().strip()
    # first_char = input("enter your nickname: ").upper()
    prediction = ""
    if first_char == "A":
        prediction = "ช้อปปิ้ง"
    elif first_char == "B":
        prediction = "อ้วน"
    elif first_char == "C":
        prediction = "โดนเท"
    elif first_char == "D":
        prediction = "แก้งาน"
    elif first_char == "E":
        prediction = "หิว"
    elif first_char == "F":
        prediction = "จน"
    elif first_char == "G":
        prediction = "มีแฟน"
    else:
        prediction = "unknown"
    print(prediction)

# %%
