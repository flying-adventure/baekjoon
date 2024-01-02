#include <stdio.h>

int main(void) {
    int num = 0;
    scanf("%d", &num);
        for (int k = num-1; k >= 0; k--) {
            for (int t = 0; t < k; t++) {
                printf(" ");
            }
            for (int p = 0; p < num-k; p++) {
                printf("*");
            }
            printf("\n");
        }
}