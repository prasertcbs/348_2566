# weight_kg=70 # snake
# height_m=1.7
gender = input("[f]emale, [m]ale ")
weight_kg = float(input("enter weight in kg. "))
height_m = float(input("enter height in m. "))
bmi = weight_kg / (height_m**2)
# linter pylint
if gender == "m":
    # literal string
    print(
        f"weight={weight_kg:.2f}, height={height_m:.2f}, bmi={bmi:.2f}"
    )  # placeholder
    if bmi >= 25:
        print("overweight")
        # target_weight_gain = weight_kg - bmi * (height_m**2)
        target_weight_gain = weight_kg - 25 * (height_m**2)
        print(f"loss {target_weight_gain:.2f} kg. to reach normal")
    elif 18.5 <= bmi < 25:
        print("normal")
    else:
        print("underweight")
        # target_weight_gain = bmi * (height_m**2) - weight_kg
        target_weight_gain = 18.5 * (height_m**2) - weight_kg
        print(f"gain {target_weight_gain:.2f} kg. to reach normal")
        # bmi=weight_kg / (height_m ** 2) # ctrl ]
        # 17=50/(1.7**2)
else:
    print(f"weight={weight_kg:.2f}, height={height_m:.2f}, {bmi:.2f}")  # placeholder
    if bmi >= 23:
        print("overweight")
        target_weight_gain = weight_kg - 23 * (height_m**2)
        print(f"loss {target_weight_gain:.2f} to reach normal")
    elif 17 <= bmi < 23:
        print("normal")
    else:
        print("underweight")
        target_weight_gain = 17 * (height_m**2) - weight_kg
        print(f"gain {target_weight_gain:.2f} to reach normal")
        # bmi=weight_kg / (height_m ** 2) # ctrl ]
        # 17=50/(1.7**2)
