#include <stdio.h>
#include <math.h>
int main(void) {
	int A[4],sum=0;
	scanf("%d %d %d %d %d", &A[0],&A[1],&A[2],&A[3],&A[4]);
	for (int y = 0; y < 5; y++) {
		sum += pow(A[y], 2);
	}
	printf("%d", sum%10);
}