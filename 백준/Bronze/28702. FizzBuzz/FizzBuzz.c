#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

void getFizzBuzz(int i, char* out) {
    if (i % 3 == 0 && i % 5 == 0)
        strcpy(out, "FizzBuzz");
    else if (i % 3 == 0)
        strcpy(out, "Fizz");
    else if (i % 5 == 0)
        strcpy(out, "Buzz");
    else
        sprintf(out, "%d", i);
}

int is_number(const char* s) {
    for (int i = 0; s[i]; i++) {
        if (!isdigit(s[i])) return 0;
    }
    return 1;
}

int main(void) {
    char a[10], b[10], c[10];
    scanf("%s %s %s", a, b, c);

    int base = -1;

    if (is_number(a)) base = atoi(a) + 3;
    else if (is_number(b)) base = atoi(b) + 2;
    else if (is_number(c)) base = atoi(c) + 1;

    char result[10];
    getFizzBuzz(base, result);
    printf("%s", result);

    return 0;
}
