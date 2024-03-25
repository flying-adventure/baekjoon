#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#define INF 99999999

typedef struct Node {
    int data;
    struct Node* next;
}Node;

typedef struct Stack {
    Node* top;
}Stack;
//push : pushes an integer onto the stack.
void push(Stack* stack, int data) {
    Node* node = (Node*)malloc(sizeof(Node));

    node->data = data;
    node->next = stack->top;
    stack->top = node;
}
//pop: Subtracts the top integer from the stack and prints the number. If there are no integers on the stack, -1 is printed.
int pop(Stack* stack) {
    if (stack->top == NULL) {
        printf("-1\n");
        return -INF;
    }
    printf("%d\n", stack->top->data);
    Node* node = stack->top;
    int data = node->data;
    stack->top = node->next;
    free(node);
    return data;
}
//size: Outputs the number of integers on the stack.
void size(Stack* stack) {
    Node* now = stack->top;
    int Size = 0;
    while (now != NULL) {
        Size++;
        now = now->next;
    }
    printf("%d\n", Size);

}
//empty: Print 1 if the stack is empty, or 0 otherwise.
int empty(Stack* stack) {
    if (stack->top == NULL) {
        printf("1\n");
        return -INF;
    }
    else {
        printf("0\n");
    }

}

//Top: Print the integer at the top of the stack. If there are no integers on the stack, print -1
void Top(Stack* stack) {
    if (stack->top == NULL) {
        printf("-1\n");
    }
    else { printf("%d\n", stack->top->data); }

}

int main() {
    Stack s;
    s.top = NULL;

    int n;
    char order[10];
    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%s", order);
        if (!strcmp(order, "push")) {
            int num;
            scanf("%d", &num);
            push(&s, num);
        }
        if (!strcmp(order, "pop")) {
            pop(&s);
        }
        if (!strcmp(order, "size")) {
            size(&s);
        }
        if (!strcmp(order, "empty")) {
            empty(&s);
        }
        if (!strcmp(order, "top")) {
            Top(&s);
        }

    }

    return 0;
}