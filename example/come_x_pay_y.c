#include <stdio.h>

int come_x_pay_y(int pax, int per_head, int come_x, int pay_y) {
  int total = (pax / come_x) * (pay_y * per_head) + (pax % come_x * per_head);
  return total;
}

int main() {
  printf("%d\n", come_x_pay_y(5, 100, 4, 3));
  return 0;
}