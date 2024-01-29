#include<stdio.h>

int main(void) {

	int bowl[101] = { 0, };
	int M, N, a, b, c;

	scanf("%d %d", &M, &N);

	for (int y = 0; y < N; y++) {
		scanf("%d %d %d", &a, &b, &c);
		for (int k=a; k <= b; k++) {
			bowl[k] = c;
		}
	}
	for (int g = 1 ; g <= M; g++) {
		printf("%d ", bowl[g]);
	}
}