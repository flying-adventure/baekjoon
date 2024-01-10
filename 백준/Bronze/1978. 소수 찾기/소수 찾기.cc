#include <stdio.h>

int main(void) {
	int cnt, result=0,num,N=0;
	scanf("%d", &cnt);
	for (int i = 0; i < cnt; i++) {
		scanf("%d", &num);
        		result = 0;

		for (int y = 1; y <= num; y++) {
			if (num % y == 0) {
				result += 1;
			}
		}
		if (result == 2) {
			N += 1;
		}
	}
	printf("%d", N);
}