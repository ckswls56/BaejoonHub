#include <stdio.h>

#define MAX_SIZE 500000 + 1
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

int Union(int x, int y)
{
    x = find(x);
    y = find(y);
    if (x == y)
    {
        return 1;
    }

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
    return 0;
}

int main()
{ //
    int n, m, res, a, b;
    scanf("%d %d", &n, &m);

    for (int i = 0; i <= n; i++)
    {
        p[i] = i; // p[i]=i 인경우 root노드
        rank[i] = 1;
    }
    res = 0;
    for (int i = 1; i <= m; i++)
    {
        scanf("%d %d", &a, &b);
        if (Union(a, b))
        {
            printf("%d",i);
            return 0;
        }
    }

    printf("%d", res);
}