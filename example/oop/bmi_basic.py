def bmi(w_kg, h_cm):
    return w_kg / (h_cm / 100) ** 2


def category(w_kg, h_cm):
    diag = ""
    bmi_value = bmi(w_kg, h_cm)
    if bmi_value < 18.5:
        diag = "ต่ำกว่าเกณฑ์"
    elif 18.5 <= bmi_value <= 25:
        diag = "ตามเกณฑ์"
    elif 25 < bmi_value <= 30:
        diag = "เกินเกณฑ์"
    elif bmi_value > 30:
        diag = "อ้วน"
    return diag


if __name__ == '__main__':
    w = 70
    h = 170
    print(bmi(w, h))
    print(category(w, h))
