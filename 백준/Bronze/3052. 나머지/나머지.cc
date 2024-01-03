#include <stdio.h>

int main(void) {
	int A, rem[42] = {0,},cnt = 0;
	for (int k = 0; k < 10; k++) {
		scanf("%d", &A);
		rem[A%42] += 1;
		
	}
	for (int p = 0; p < 42; p++) {
		if (rem[p] != 0) {
			cnt += 1;
		}
	}
	printf("%d", cnt);
}