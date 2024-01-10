
#include <stdio.h>

int main(void) {
	int cnt, score[1001], max = 0;
	double sum = 0;
	scanf("%d", &cnt);
	for (int u = 0; u < cnt; u++) {
		scanf("%d", &score[u]);
		if (score[u] > max) {
			max = score[u];
		}
	}
	for (int u = 0; u < cnt; u++) {
			sum += ((double)score[u] / max) * 100;
	}
	printf("%f",(double) sum / cnt);
}