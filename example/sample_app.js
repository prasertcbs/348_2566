'use strict';

function rectangle(w, h) {
    return w * h
}

function square(s) {
    return rectangle(s, s)
}

function triangle(b, h) {
    return rectangle(b, h) * .5
}

function mecard(name, email, phone) {
    return `MECARD:N:${name};EMAIL:${email};TEL:${phone};`
}

console.log(rectangle(5, 3));
console.log(square(5));
console.log(triangle(5, 3));
console.log(mecard('Peter', 'peter@marvel.com', '088-123-7788'))
