package main

import "fmt"

func come_x_pay_y(pax int, per_head int, come int, pay int) int {
	amt := (pax / come) * (pay * per_head) + (pax % come) * per_head
	return amt
}

func main() {
	fmt.Println(come_x_pay_y(5, 100, 4, 3))
}