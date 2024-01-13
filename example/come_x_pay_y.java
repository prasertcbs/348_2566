public class come_x_pay_y {
	public static int come_x_pay_y(int pax, int per_head, int come_x, int pay_y) {
		int total = (pax / come_x) * (pay_y * per_head) + (pax % come_x * per_head);
	return total;
	}

	public static void main(String[] args) {
		System.out.println(come_x_pay_y(5, 100, 4, 3));
	}
}