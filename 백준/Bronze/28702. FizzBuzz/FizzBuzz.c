#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// FizzBuzz 규칙에 따라 숫자 i의 출력 문자열을 구함
void getFizzBuzz(int i, char* out) {
    if (i % 3 == 0 && i % 5 == 0)
        strcpy(out, "FizzBuzz");
    else if (i % 3 == 0)
        strcpy(out, "Fizz");
    else if (i % 5 == 0)
        strcpy(out, "Buzz");
    else
        sprintf(out, "%d", i);  // 숫자를 문자열로 변환
}

int main(void) {
    //입력받기
    char a[10], b[10], c[10];
    scanf("%s %s %s", a, b, c);

    int base = -1;

    // 입력 중 숫자인 줄을 찾고, 해당 위치에 따라 다음 출력 위치 계산
    if (isdigit(a[0])) base = atoi(a) + 3;
    else if (isdigit(b[0])) base = atoi(b) + 2;
    else if (isdigit(c[0])) base = atoi(c) + 1;

    // 다음 출력 결과 구하기
    char result[10];
    getFizzBuzz(base, result);

    // 결과 출력
    printf("%s\n", result);

    return 0;
}
