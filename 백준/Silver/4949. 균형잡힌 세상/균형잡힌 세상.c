#include<stdio.h>
#include<string.h>

int key = -1;

int push(char stack[], char bal) {
	stack[++key] = bal;
}

int pop() {
	key--;
}

int main(void) {
	while (1) {
		key = -1;
		char stack[100];
		char str[102];
		scanf("%[^\n]s", str);
		if (str[0] == '.') break;
		for (int k = 0; k < 102; k++) {
			if (str[k] == '(')push(stack, '(');
			else if (str[k] == '[')push(stack, '[');
			else if (str[k] == ')') {
				if (stack[key] == '(')pop();
				else { printf("no\n"); break; }
			}
			else if (str[k] == ']') {
				if (stack[key] == '[')pop();
				else { printf("no\n"); break; }
			}
			if (str[k] == '.') {
				if (key == -1) {
					printf("yes\n"); break;
				}
				else { printf("no\n"); break; }
			}
		}getchar();

	}
	
}