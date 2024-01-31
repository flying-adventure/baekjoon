#include<stdio.h>

int main(void) {
	int m, n;
	scanf("%d %d", &n, &m);
	int bowl[101] = { 0, };
	for (int y = 1; y <= n; y++) {
		bowl[y] = y;
	}

	int i, j;
	for (int a = 0; a < m; a++)
	{
		scanf("%d %d", &i, &j);
		int temp = 0;
		for (i; i < j; i++)
		{
			temp = bowl[i];
			bowl[i] = bowl[j];
			bowl[j] = temp;
			j--;			
		}
	}

	for (int r = 1; r <= n; r++) {
		printf("%d ", bowl[r]);
	}
}