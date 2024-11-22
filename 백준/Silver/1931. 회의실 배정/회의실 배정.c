#include<stdio.h>
#include <stdlib.h>
int N=0; //회의의 수

// 회의 구조체 정의
typedef struct {
    int start;
    int end;
} Meeting;

// 종료 시간 기준으로 정렬하기 위한 비교 함수
int compare(const void *a, const void *b) {
    Meeting *m1 = (Meeting *)a;
    Meeting *m2 = (Meeting *)b;
    if (m1->end == m2->end) {
        return m1->start - m2->start; // 종료 시간이 같으면 시작 시간으로 정렬
    }
    return m1->end - m2->end; // 종료 시간 기준 정렬
}
int main(){
    scanf("%d",&N);
    Meeting meetings[N];
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &meetings[i].start, &meetings[i].end);
    }

    // 종료 시간 기준으로 정렬
    qsort(meetings, N, sizeof(Meeting), compare);

    int count = 0;    // 최대 회의 개수
    int last_end = 0; // 마지막으로 선택한 회의의 종료 시간

    for (int i = 0; i < N; i++) {
        if (meetings[i].start >= last_end) { // 겹치지 않는 회의만 선택
            count++;
            last_end = meetings[i].end;
        }
    }

    printf("%d\n", count);
    return 0;
}