#include<stdio.h>
int main(void) {
	/* 어떤 자연수 p와 q가 있을 때,
	만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 
	두 개의 자연수 N과 K가 주어졌을 때, 
	N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오. */ 

	int n,k;
	int key=1;
	scanf("%d %d", &n, &k);
	for (int i = 1; i <= n; i++) {
		if (n % i == 0) {
			if (key == k) {
				printf("%d", i);
				return 0;
			}
            key++;
		}
	}
    printf("0");

}