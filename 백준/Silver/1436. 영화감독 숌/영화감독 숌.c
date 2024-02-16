#include<stdio.h>
int main(void) {
	int n;
	scanf("%d", &n);
	int num = 666, count=0;

	while (1) {
		int cnt_6 = 0;
        int over=num;
		while (over > 0) {
            int digit=over%10;
			if (digit == 6) cnt_6++;
            else cnt_6=0;
			if (cnt_6 == 3) { count++; break; }
			over /= 10;
		}
		if (count == n)break;
        num++;
	}
    printf("%d", num);
}