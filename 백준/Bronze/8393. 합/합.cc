#include <stdio.h>
int main(void) {
	int num,sum=0;
	scanf("%d", &num);
	for (int y = 0; y <= num; y++) {
		sum += y;
	}
	printf("%d", sum);
}