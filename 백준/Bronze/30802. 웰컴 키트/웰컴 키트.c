#include <stdio.h>

int main(void) {
    int N;
    scanf("%d", &N);

    int s[6];
    for (int i = 0; i < 6; i++) {
        scanf("%d", &s[i]);
    }

    int T, P;
    scanf("%d %d", &T, &P);

    int tshirt_bundle_count = 0;
    for (int i = 0; i < 6; i++) {
        tshirt_bundle_count += (s[i] + T - 1) / T;  // 정수 올림 계산
    }

    int pen_bundle = N / P;
    int pen_single = N % P;

    printf("%d\n", tshirt_bundle_count);
    printf("%d %d\n", pen_bundle, pen_single);

    return 0;
}