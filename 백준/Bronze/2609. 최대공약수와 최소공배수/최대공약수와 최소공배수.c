#include<stdio.h>

int main() {
	int x, y;
	scanf("%d %d", &x, &y);
	int e, c;
	int big,small;
	if (x >= y) {
		big = x;
		small = y;
	}
	else {
		big = y;
		small = x;
	}

	for (int u = 1; u <= small;u++) {
		if (small % u == 0) {
			if (big % u == 0) {
				e = u;
			}
		}
	}//최대 공약수
	c = (x * y) / e; //최소공배수

	printf("%d\n%d", e,c );
	return 0;


}