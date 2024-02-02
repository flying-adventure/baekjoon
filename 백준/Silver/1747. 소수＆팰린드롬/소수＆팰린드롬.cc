#include <stdio.h>
#include <stdbool.h>


bool isPrime(int num);
bool isPalindrome(int num);

int main() {
    int N;

    scanf("%d", &N);
      
    while (1) {
        if (isPrime(N) && isPalindrome(N)) {
            printf("%d", N);
            break;
        }
        N++;
    }return 0;
}


bool isPrime(int num) {
    if (num < 2) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}


bool isPalindrome(int num) {
    int original = num;
    int reversed = 0;

    while (num > 0) {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    }
    return original == reversed;
}