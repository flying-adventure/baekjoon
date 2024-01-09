#include <stdio.h>
int main(void) {
	int num[8];
	for (int i = 0; i < 8; i++) {
		scanf("%d", &num[i]);
	}
	for (int y = 0; y < 8; y++) {
		if (num[y] != y + 1) {
			break;
		}
		if(y==7){
			printf("ascending\n");
			return 0;
		}
	}
	for (int y = 0; y < 8; y++) {
		if (num[y] != 8 - y) {
			break;
		}
		if(y==7){
			printf("descending\n");
			return 0;
		}
	}
		printf("mixed\n");
}