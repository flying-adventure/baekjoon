#include <stdio.h>

int main(void) {
	int num;
	scanf("%d", &num);
	for (int k = 1; k <= 9; k++) {
		printf("%d * %d = %d\n", num, k, num * k);
	}
}