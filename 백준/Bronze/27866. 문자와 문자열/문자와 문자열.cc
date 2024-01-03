#include <stdio.h>
int main(void) {
	char m[1000];
	int n;
	
	scanf("%s", m);

	scanf("%d", &n);
	printf("%c", m[n-1]);

}