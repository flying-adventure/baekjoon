#include <stdio.h>
int main(void) {
	int X,N,a, b,price=0;
	scanf("%d", &X);
	scanf("%d", &N);
	for (int y = 0; y < N; y++) {
		scanf("%d %d", &a, &b);
		price += a * b;
	}
	if (X == price) {
		printf("Yes");
	}
	else { printf("No"); }

}