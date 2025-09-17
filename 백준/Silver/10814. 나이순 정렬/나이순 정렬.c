#include<stdio.h>
#include<stdlib.h>

typedef struct {
	int age;
	char name[101];
	int order;
}Person;
int compare(const void* a, const void* b) {
	Person* PersonA = (Person*)a;
	Person* PersonB = (Person*)b;

	if (PersonA->age != PersonB->age) {
		return PersonA->age - PersonB->age;
	}
	else {
		return PersonA->order - PersonB->order;
	}

	
}
int main() {

	int N;
	Person members[100000];
	
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d %s", &members[i].age, members[i].name);
		members[i].order = i;
	}
	qsort(members, N, sizeof(Person), compare);
	for (int i = 0; i < N; i++) {
		printf("%d %s\n", members[i].age, members[i].name);
	}

	
	
	
}