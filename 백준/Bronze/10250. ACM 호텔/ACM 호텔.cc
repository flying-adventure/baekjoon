#include <stdio.h>

int main(void) {
	int t, H, W, N;
	scanf("%d", &t);
	while (1) {
		int room = 1;
		scanf("%d %d %d", &H, &W, &N);
		if (N % H != 0) {
			room += 100 * (N % H) + (N / H);
			printf("%d\n", room);
		}
		else {
			room += 100*H + (N / H)-1;
            printf("%d\n", room);
		}
		
		t--;
		if (t == 0) {
			break;
		}
	}
}