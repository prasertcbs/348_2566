def come_x_pay_y(pax, per_head, come_x=4, pay_y=3):
    total = (pax // come_x) * (pay_y * per_head) + (pax % come_x * per_head)
    return total


print(come_x_pay_y(5, 100, 4, 3))
