#include <stdio.h>

int main(void){
    int n;
    int a=0,b=0;
    int result;

    scanf("%d",&n);

    for(int i=2;i<=n;i++){
        int x = i;
        while(x%2==0){
            x/=2;
            a++;
        }
        while(x%5==0){
            x/=5;
            b++;
        }
    }

    if(a<b) result = a;
    else result = b;

    printf("%d",result);
}