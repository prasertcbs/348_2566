# NATO phonetic alphabet
# ref: http://www.osric.com/chris/phonetic.html
def convert(s):
    p = {"A": "Alpha",
         "B": "Bravo",
         "C": "Charlie",
         "D": "Delta",
         "E": "Echo",
         "F": "Foxtrot",
         "G": "Golf",
         "H": "Hotel",
         "I": "India",
         "J": "Juliet",
         "K": "Kilo",
         "L": "Lima",
         "M": "Mike",
         "N": "November",
         "O": "Oscar",
         "P": "Papa",
         "Q": "Quebec",
         "R": "Romeo",
         "S": "Sierra",
         "T": "Tango",
         "U": "Uniform",
         "V": "Victor",
         "W": "Whiskey",
         "X": "X-ray",
         "Y": "Yankee",
         "Z": "Zulu"}
    w = []
    for c in s:
        w.append(p[c.upper()])
    return " ".join(w)


nato = convert("thailand")
print(nato)
