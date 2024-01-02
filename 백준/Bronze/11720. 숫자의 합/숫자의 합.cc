#include<stdio.h>

//N개의 숫자가 공백 없이 쓰여있다. 
// 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.


int main(){
    int n, sum = 0;
    scanf("%d", &n);
    char arr[n];
    scanf("%s", &arr);
    for(int i = 0; i < n; i++){
        sum += arr[i] - '0';
    }
    printf("%d", sum);
}