#include<stdio.h>
// 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 
// X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
int main(void) {
	int N,X;

	scanf("%d %d", &N, &X);
	int A[10000] = { 0, };
	for (int j = 0; j < N; j++) {
		scanf("%d", &A[j]);
		if (X > A[j]) {
			printf("%d ", A[j]);
		}
	}

}