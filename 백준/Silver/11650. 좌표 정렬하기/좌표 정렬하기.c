#include <stdio.h>
#include<stdlib.h>

typedef struct {
	int x;
	int y;
}xy;

int compare(const void* a, const void* b) {
	xy* xyA = (xy*)a;
	xy* xyB = (xy*)b;
	if(xyA->x!=xyB->x){
		return xyA->x - xyB->x;
	}
	else {
		return xyA->y - xyB->y;
	}
}

int main() {
	int N;
	scanf("%d", &N);

	xy locate[100000];

	for (int i = 0; i < N; i++) {
		scanf("%d %d", &locate[i].x, &locate[i].y);
	}
	qsort(locate, N, sizeof(xy), compare);
	for (int i = 0; i < N; i++) {
		printf("%d %d\n", locate[i].x, locate[i].y);
	}

}