#include<stdio.h>
#include<string.h>

int number[100001];
int cnt = -1;


//empty: Print 1 if the stack is empty, or 0 otherwise.
int empty() {
	if (cnt == -1) {
		return 1;
	}
	else { return 0; }
}

//push X: pushes an integer X onto the stack.
int push_X(int num) {
	cnt++;
	number[cnt] = num;
}

//pop: Subtracts the top integer from the stack and prints the number. If there are no integers on the stack, -1 is printed.
int pop() {
	int k = empty();
	if (k == 1) { printf("-1\n"); }
	else {
		printf("%d\n", number[cnt]);
		number[cnt] = 0;
		cnt--;
	}
}

//size: Outputs the number of integers on the stack.
int size() {
	if (cnt == -1) {
		printf("0\n");
	}
	else {
		printf("%d\n", cnt + 1);
	}
}

//top: Print the integer at the top of the stack. If there are no integers on the stack, print -1
int top() {
	int k = empty();
	if (k == 1) {
		printf("-1\n");
	}
	else {
		printf("%d\n", number[cnt]);
	}

}
int main(void) {
	int n;
	char order[10];
	scanf("%d", &n);
	for (int k = 0; k < n; k++) {

		scanf("%s", order);
		if (!strcmp(order, "push")) {
			int num;
			scanf("%d", &num);
			push_X(num);
		}
		if (!strcmp(order, "pop")) {
			pop();
		}
		if (!strcmp(order, "size")) {
			size();
		}
		if (!strcmp(order, "empty")) {
			int p = empty();
			printf("%d\n", p);
		}
		if (!strcmp(order, "top")) {
			top();
		}
	}

}