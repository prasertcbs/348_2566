function come_x_pay_y(pax, per_head, come, pay) {
    let amt = Math.floor(pax / come) * (pay * per_head) + (pax % come) * per_head;
    return amt;
}

console.log(come_x_pay_y(5, 100, 4, 3));
