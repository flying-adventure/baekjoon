#include <stdio.h>
#include <stdlib.h>

typedef int Data;

typedef struct _bTreeNode
{
	Data data;
	struct _bTreeNode* left;
	struct _bTreeNode* right;

} Node;

typedef void VisitFuncPtr(Data data);

Node* MakeBTreeNode(Data data)
{
	Node* nd = (Node*)malloc(sizeof(Node));
	nd->data = data;
	nd->left = NULL;
	nd->right = NULL;
	return nd;
}

void Postorder(Node* bt)
{
	if (bt == NULL)
		return;
	Postorder(bt->left);
	Postorder(bt->right);
	printf("%d\n", bt->data);
}

Node* AssignTree(Node* bt, Data data) {
	if (bt == NULL) {
		bt = MakeBTreeNode(data);
		return bt;
	}
	else if (data < bt->data)
	{
		bt->left = AssignTree(bt->left, data);
	}
	else if (data > bt->data)
	{
		bt->right = AssignTree(bt->right, data);
	}
	return bt;
}


int main(void)
{
	int k;
	Node* bt = NULL;
	while (scanf("%d", &k) != EOF)
	{
		bt = AssignTree(bt, k);
	}
	Postorder(bt);
}