fn come_x_pay_y(pax: i32, per_head: i32, come: i32, pay: i32) -> i32 {
	let amt = (pax / come) * (pay * per_head) + (pax % come) * per_head;
	return amt;
}

fn main() {
	println!("{}", come_x_pay_y(5, 100, 4, 3));
	// println!("{}", come_x_pay_y(5, 100));
}