#include <stdio.h>

int main(void)
{
	int day, A, B, V;
	scanf("%d %d %d", &A, &B, &V);
    
	day = (V - A) / (A - B) + 1;
	if ((V - A) % (A - B) != 0){day += 1;}
	printf("%d", day);
	
}
