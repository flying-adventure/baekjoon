#include<stdio.h>

int main(void) {
	//자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 
	// 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

	int m, n; //m<=n
	int sum=0; //소수의 합
    int is=0;

	scanf("%d", &m);
	scanf("%d", &n);
	int min = n; //최솟값

	for (int i = m; i <= n; i++) {
		for (int k = 2; k <= i; k++) {
			if (k == i) {
                //printf("%d\n",k);
				sum += k;
                is=1;
				if (k <= min) {
					min = k;
				}
			}
			if (i % k == 0) {
				break;
			}
		}
	}
    //단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
    if(is==0){printf("-1");return 0;}
	printf("%d\n%d", sum, min);

}