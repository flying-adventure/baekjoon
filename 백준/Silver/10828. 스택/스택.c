#include<stdio.h>
#include<string.h>

int number[100001];
int cnt = -1;


//스택이 비어있으면 1, 아니면 0을 출력한다.
int empty() {
	if (cnt == -1) {
		return 1;
	}
	else { return 0; }
}

//정수 X를 스택에 넣는 연산이다.
int push_X(int num) {
    cnt++;
	number[cnt] = num;
}

//스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
int pop() {
int k=empty();
if(k==1){printf("-1");}
else{
printf("%d",number[cnt]);
	number[cnt] = 0;
	cnt--;
}

}

//스택에 들어있는 정수의 개수를 출력한다.
int size() {
if(cnt==-1){
printf("0");}else{
	printf("%d", cnt+1);
}
}

//스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
int top() {
	int k = empty();
	if (k == 1) { 
		printf("-1");
	}
	else {
		printf("%d", number[cnt]);
	}
	
}
int main(void) {
	int n;
	char order[10];
    scanf("%d",&n);
	for (int k = 0; k < n; k++) {

		scanf("%s", order);
		if (!strcmp(order,"push")) {
			int num;
			scanf("%d", &num);
			push_X(num);
		}
		if (!strcmp(order,"pop")) {

			pop();
            printf("\n");
		}
		if (!strcmp(order,"size")) {

			size();
            printf("\n");
		}
		if (!strcmp(order,"empty")) {
 
			int p=empty();
            printf("%d\n",p);

		}
		if (!strcmp(order,"top")) {

			top();
            printf("\n");

		}
	}

}