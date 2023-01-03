# pip install qrcode Pillow
import qrcode


def mecard(fname, lname, email, tel):
    # https://en.wikipedia.org/wiki/MeCard_(QR_code)
    # MECARD:N:Doe,John;TEL:13035551212;EMAIL:john.doe@example.com;;
    me = f"MECARD:N:{fname} {lname};TEL:{tel};EMAIL:{email};"
    print(me)
    img = qrcode.make(me)
    return img


if __name__ == "__main__":
    # img = qrcode.make('I love Python??')
    # img.show()
    # img.save('demo.png')
    q = mecard("Peter", "Parker", "peter@umail.com", "099-111-2233")
    q.save("mecard.png")
    q.show()
