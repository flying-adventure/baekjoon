#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
	int data;
	struct Node* next;
}Node;

Node* front = NULL;
Node* rear = NULL;

void enqueue(int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	if (newNode == NULL) {
		return;
	}
	newNode->data = data;
	newNode->next = NULL;

	if (rear == NULL) {  //큐가 비어있는 경우
		front = newNode;
		rear = newNode;
	}
	else { //큐에 이미 노드가 있는 경우
		rear->next = newNode;
		rear = newNode;
	}
}
int dequeue() {
	if (front == NULL) { // 큐가 비어있는 경우
		return -1; // 또는 다른 오류 처리
	}
	Node* temp = front;
	int data = temp->data;
	front = front->next;

	if (front == NULL) { // 마지막 노드를 꺼낼 경우
		rear = NULL;
	}
	free(temp); // 사용한 메모리 해제
	return data;
}
int main() {
	int N;
	scanf("%d", &N);

	// 1부터 N까지 카드를 큐에 추가
	for (int i = 1; i <= N; i++) {
		enqueue(i);
	}

	// 큐에 한 장의 카드가 남을 때까지 반복
	while (front != rear) {
		// 첫 번째 카드 버리기
		dequeue();

		// 다음 카드 맨 뒤로 옮기기
		int cardToMove = dequeue();
		enqueue(cardToMove);
	}

	// 마지막으로 남은 카드 출력
	printf("%d\n", front->data);

	// 큐 메모리 정리
	dequeue(); // 마지막 노드 정리

	return 0;
}