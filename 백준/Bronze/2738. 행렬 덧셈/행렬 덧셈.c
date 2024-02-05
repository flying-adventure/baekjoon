#include<stdio.h>

int main(void) {
	int m, n;
	scanf("%d %d", &n, &m);
	int a[100][100], b[100][100];
    
	for (int r = 0; r < n; r++) {
		for (int e = 0; e < m; e++) {
			scanf("%d", &a[r][e]);
		}
	}
	for (int r = 0; r < n; r++) {
		for (int e = 0; e < m; e++) {
			scanf("%d", &b[r][e]);
		}
	}
	int sum = 0;
	for (int i = 0; i < n; i++) {
		for (int y = 0; y < m; y++) {
			sum = a[i][y] + b[i][y];
			printf("%d ", sum);
		}
		printf("\n");
	}
}