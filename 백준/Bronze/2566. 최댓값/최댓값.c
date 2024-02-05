#include<stdio.h>
int main(void) {
	int arr[9][9];
	for (int y = 0; y < 9; y++) {
		scanf("%d %d %d %d %d %d %d %d %d", &arr[y][0], &arr[y][1], &arr[y][2], &arr[y][3], &arr[y][4], &arr[y][5], &arr[y][6], &arr[y][7], &arr[y][8] );
	}
	int max = 0,h=0,w=0;
	for (int f = 0; f < 9; f++) {
		for (int g = 0; g < 9; g++) {
			if (max <= arr[f][g]) {
				max = arr[f][g];
				h = f+1;
				w = g+1;
			}
		}
	}
	printf("%d\n%d %d",max, h, w);

}