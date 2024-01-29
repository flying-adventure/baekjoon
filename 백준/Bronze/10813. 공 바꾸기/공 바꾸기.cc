#include<stdio.h>

int main(void) {
	int N[101],M,n;
	scanf("%d %d", &n,&M);
	for (int y = 0; y <= n; y++) {
		N[y] = y;
	}
	int temp,a, b;
	for (int u = 0; u < M; u++) {
		scanf("%d %d", &a, &b);
		temp = N[a];
		N[a] = N[b];
		N[b] = temp;
	}
	for (int e = 1; e <= n; e++) {
		printf("%d ", N[e]);
	}
}