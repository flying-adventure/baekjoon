#include <stdio.h>

int main() {
    int n, newNum, count = 0;
    int original; 

    scanf("%d", &n);
    original = n; // 초기값 저장

    do {
        int sum = (n / 10) + (n % 10); // 각 자리 숫자 합
        newNum = (n % 10) * 10 + (sum % 10); // 새로운 수 생성
        n = newNum; // 새로운 수를 다시 n에 저장
        count++;
    } while (newNum != original); // 원래 숫자로 돌아올 때까지 반복

    printf("%d\n", count); // 사이클 길이 출력
    return 0;
}