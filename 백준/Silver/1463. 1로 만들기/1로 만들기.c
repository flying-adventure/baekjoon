#include<stdio.h>

int dp[1000001];
int MIN(int x, int y) {
	return (x < y) ? x : y;
}
int main() {
	int num;
	scanf("%d", &num);
	for (int i = 2; i <= num; i++) {
		dp[i] = dp[i - 1] + 1;
		if (i % 2 == 0) { dp[i] = MIN(dp[i], dp[i / 2] + 1); }
		if (i % 3 == 0) { dp[i] = MIN(dp[i], dp[i / 3] + 1); }
	}
	printf("%d", dp[num]);
	return 0;
}