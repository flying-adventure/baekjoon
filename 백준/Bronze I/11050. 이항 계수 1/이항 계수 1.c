#include<stdio.h>
int factorial(int num) {
	int result = 1;
	for (int i = 1; i <= num; i++) {
		result = result * i;
	}
	return result;
}
int main(void) {
	//n C k
	int n, k;
	scanf("%d %d", &n, &k);
	int a = factorial(n);
	int b = factorial(k);
	int c = factorial(n - k);
	int result = a / (b * c);
	printf("%d", result);

}