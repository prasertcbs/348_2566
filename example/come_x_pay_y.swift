//header for function
import Foundation

func come_x_pay_y(pax: Int, per_head: Int, come: Int = 4, pay: Int = 3) -> Int {
	let amt = (pax / come) * (pay * per_head) + (pax % come) * per_head
	return amt
}

print(come_x_pay_y(pax: 5, per_head: 100, come: 4, pay: 3))
print(come_x_pay_y(pax: 5, per_head: 100))