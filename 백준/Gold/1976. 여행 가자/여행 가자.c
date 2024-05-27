#include <stdio.h>
#define INF 1000005

int p[INF] = { 0 };
int n, m;

void fillp(int n) {
    for (int i = 0; i <= n; i++) 
        p[i] = i;
}

int find(int n) {
    if (p[n] == n) return n;
    else return p[n] = find(p[n]);
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    p[b] = a;
}

int main(void) {
    int a;
    scanf("%d %d", &n, &m);
    fillp(n);

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            scanf("%d", &a);
            if (a == 1)
                merge(i, j);
        }
    }

    int start, cnt = 0;
    scanf("%d", &start);

    for (int i = 1; i < m; i++) {
        scanf("%d", &a);
        if (find(start) == find(a)) {
            cnt++;
        } else break;
        start = a;
    }

    if (cnt == m - 1) printf("YES\n");
    else printf("NO\n");

    return 0;
}