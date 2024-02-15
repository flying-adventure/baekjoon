#include<stdio.h>

int main(void) {
	//N개의 수가 주어졌을 때, 
	//이를 오름차순으로 정렬하는 프로그램을 작성하시오.
    // 숫자를 모두 저장해놓으면 메모리 초과가 난다. 하나 입력받고 하나 처리하고,,해야함

	int n;
	scanf("%d", &n);
    int num=0;
    int arr[10001]={0,};
    
	for(int i=0;i<n;i++){
        scanf("%d",&num);
        arr[num]++;
    }
    for(int i=0;i<10001;i++){
        if(arr[i]!=0){
            for(int y=arr[i];y>0;y--){
            printf("%d\n",i);
            }
        }
    }
}