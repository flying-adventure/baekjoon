#include <stdio.h>
#include <string.h>

int main(void) {
    char input[15];        
    int digits[13];
    int star_index = 0;

    scanf("%s", input, 15); 

    for (int i = 0; i < 13; i++) {
        if (input[i] == '*') {
            digits[i] = 0;
            star_index = i;
        } else {
            digits[i] = input[i] - '0';
        }
    }

    int ISBM = 0;
    for (int i = 0; i < 13; i++) {
        if (i == star_index) continue; 
        ISBM += (i % 2 == 0) ? digits[i] : 3 * digits[i];
    }

    for (int i = 0; i < 10; i++) {
        int delta = (star_index % 2 == 0) ? i : 3 * i;
        if ((ISBM + delta) % 10 == 0) {
            printf("%d\n", i); 
            return 0;
        }
    }
}
