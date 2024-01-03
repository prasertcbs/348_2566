function come_x_pay_y(pax, per_head, come=4, pay=3) {
    let amt = Math.floor(pax / come) * (pay * per_head) + (pax % come) * per_head;
    return amt;
}

console.log(come_x_pay_y(5, 100, 4, 3));
console.log(come_x_pay_y(5, 100));
