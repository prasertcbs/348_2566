#include <cmath>
#include <iostream>
using namespace std;

int come_x_pay_y(int pax, int per_head, int come = 4, int pay = 3) {
  int amt = floor(pax / come) * (pay * per_head) + (pax % come) * per_head;
  return amt;
}

int main() {
  cout << come_x_pay_y(5, 100, 4, 3) << endl;
  cout << come_x_pay_y(5, 100) << endl;
}