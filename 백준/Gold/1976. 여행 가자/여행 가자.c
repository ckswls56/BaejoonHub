#include <stdio.h>

#define MAX_SIZE 200 + 1
int p[MAX_SIZE];
int rank[MAX_SIZE];

int find(int x)
{
    if (x == p[x])
        return x;
    else
    {
        int y = find(p[x]);
        p[x] = y;
        return y;
    }
}

void Union(int x, int y)
{
    x = find(x);
    y = find(y);
    if (x == y)
        return;

    if (rank[x] > rank[y])
    {
        p[y] = x;
        rank[x] += rank[y];
    }
    else
    {
        p[x] = y;
        rank[y] += rank[x];
    }
}

int main()
{
    int n, m, x;
    int travel[1001];
    scanf("%d %d", &n, &m);

    for (int i = 0; i <= n; i++)
    {
        p[i] = i; // p[i]=i 인경우 root노드
        rank[i] = 1;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            scanf("%d", &x);
            if (x)
            {
                Union(i, j);
            }
        }
    }

    for (int i = 0; i < m; i++)
    {
        scanf("%d", &travel[i]);
    }

    for (int i = 0; i < m - 1; i++)
    {
        if (find(travel[i]) != find(travel[i + 1]))
        {
            printf("NO");
            return 0;
        }
    }
    printf("YES");
}