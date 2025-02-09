#include <stdio.h>
int main(void){
    int n;
    scanf("%d",&n);
    for(int k=0;k<n;k++){
        int a=0,b=0;
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);
    }
}