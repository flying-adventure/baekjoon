#include <stdio.h>

typedef struct {
    int weight;
    int height;
} Person;

int main() {
    int N;
    scanf("%d", &N);
    Person people[50];

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &people[i].weight, &people[i].height);
    }

    for (int i = 0; i < N; i++) {
        int rank = 1; 
        for (int j = 0; j < N; j++) {
            if (i == j) continue; 
            if (people[j].weight > people[i].weight && people[j].height > people[i].height) {
                rank++;
            }
        }
        printf("%d ", rank);
    }

    return 0;
}
