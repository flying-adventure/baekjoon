#include <stdio.h>

int main(void) {
    int N;
    scanf("%d", &N);

    int num = -1;
    int max = N / 5; 

    for (int i = max; i >= 0; i--) {
        if ((N - i * 5) % 3 == 0) {
            num = i + (N - i * 5) / 3;
            break;
        }
        else {
            if (i == 0)
                break;
            else
                continue;
        }
    }
    printf("%d", num);
}