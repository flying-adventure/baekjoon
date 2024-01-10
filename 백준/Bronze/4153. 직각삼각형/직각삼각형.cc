#include <stdio.h>
#include <math.h>

int main(void) {
	while (1) {
		int num[3], max = 0, sum = 0 ,max_po=0;

		for (int y = 0; y < 3; y++) {
			scanf("%d", &num[y]);
			if (max < num[y]) {
				max = num[y];
			}
		}
		if (num[0] == 0) {
			break;
		}
		max_po = pow(max, 2);
		for (int y = 0; y < 3; y++) {
			if (num[y] < max) {
				sum += pow(num[y], 2);
			}
		}
		if (max_po == sum) {
			printf("right\n");
		}
		else { printf("wrong\n"); }
	}
}