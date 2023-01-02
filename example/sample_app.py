def rectangle(w, h):
    return w * h

def square(s):
    return rectangle(s, s)

def triangle(b, h):
    return rectangle(b, h) * .5

def mecard(name, email, phone):
    return f'MECARD:N:{name};EMAIL:{email};TEL:{phone};'

print(rectangle(5, 3))
print(square(5))
print(triangle(5, 3))
print(mecard('Peter', 'peter@marvel.com', '088-123-7788'))
