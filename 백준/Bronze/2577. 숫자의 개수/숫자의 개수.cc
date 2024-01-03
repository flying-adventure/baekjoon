#include<stdio.h>

int main(void) {
	int A, B, C, cnts[10] = { 0, };
	scanf("%d", &A);
	scanf("%d", &B);
	scanf("%d", &C);
	int mul = A * B * C;
	while (mul > 0) {
		int cnt = mul % 10;
		cnts[cnt] += 1;
		mul = mul / 10;
	}
	for (int k = 0; k < 10; k++) {
		printf("%d\n", cnts[k]);
	}

}