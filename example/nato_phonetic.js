'use strict';

function convert(s) {
    let p = {
        "A": "Alpha",
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
        "Z": "Zulu"
    }
    let nato_text=''
    let w=[]
    for (let i = 0; i < s.length; i++) {
        // nato_text += p[s[i].toUpperCase()];
        w.push(p[s[i].toUpperCase()]);
    }
    // return nato_text
    return w.join(' ')
}

function foo(s) {
    s.split("").forEach((item, index)=>console.log(s[index]));
}

// foo('peter')
let nato = convert("thailand")
console.log(nato);
