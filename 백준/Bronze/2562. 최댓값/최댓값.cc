#include <stdio.h>

int main(void) {
	int n[9],big=0,pos=0;
	for (int k = 0; k < 9; k++) {
		scanf("%d", &n[k]);
		if (n[k] >= big) {
			big = n[k];
			pos = k;
		}
		else { continue; }
	}
	printf("%d\n", big);
	printf("%d", pos+1);

}