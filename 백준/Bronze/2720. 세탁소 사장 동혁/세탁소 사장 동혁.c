#include<stdio.h>
int main(void) {
	int k,ch;
	scanf("%d", &k);
    
	for (int u = 0; u < k; u++) {
        	int q = 0, d = 0,n = 0, p = 0;
		scanf("%d", &ch);
		while (ch >= 25) {
			q++;
			ch -= 25;
		}
		while (ch >= 10) {
			d++;
			ch -= 10;
		}
		while (ch >= 5) {
			n++;
			ch -= 5;
		}
		while (ch >= 1) {
			p++;
			ch -= 1;
		}

		printf("%d %d %d %d\n", q, d, n, p);
	}

}