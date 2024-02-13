#include <stdio.h>

int main(void)
{
	int n, num = 2;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		num = num + (num - 1);
	}
	printf("%d", num * num);
	return 0;
}
