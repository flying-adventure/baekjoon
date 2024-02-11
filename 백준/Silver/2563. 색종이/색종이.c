#include<stdio.h>
int main(void) {
	int arr[101][101] = {0,};
	int n;
	scanf("%d", &n);
	int w, h,cmt=0;

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &w, &h);
		for (int x = w; x < w + 10; x++) {
			for (int y = h; y < h + 10; y++) {
				arr[x][y] = 1;

			}
		}
	}
	for (int x = 1; x < 101; x++) {
		for (int y = 1; y < 101; y++) {
			if (arr[x][y] == 1) {
				cmt++;
			}
		}
	}
	printf("%d", cmt);
}