# logical operators
# and, or, not
# %%
is_cbs_student = True # boolean
is_mis_student = True
price = 50
discount_pct = .2
if is_cbs_student == True and is_mis_student == True:
    print(price, price * (1-discount_pct))

if is_cbs_student and is_mis_student:
    print(price, price * (1-discount_pct))
    
# %%
toefl = 80
ielts = 4.5
is_us_citizen = True
if toefl > 85 or ielts > 6 or is_us_citizen:
    print("pass")
else:
    print("fail")

white_skin = False
height = 1.6 # above 1.65
good_look = True
is_smoker = True

if ((white_skin and height == 1.65) or good_look) and not is_smoker:
    print("date me")
else:
    print("sorry, not my spec")

if (white_skin and height >= 1.65) or good_look:
    print("date me")
else:
    print("sorry, not my spec")

if good_look or (white_skin and height >= 1.65):
    print("date me")
else:
    print("sorry, not my spec")

if (good_look or white_skin) and height >= 1.65:
    print("date me")
else:
    print("sorry, not my spec")

print(not is_smoker)