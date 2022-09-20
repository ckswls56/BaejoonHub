#include <iostream>
#include <utility>
#include <tuple>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#define MAX_V 10000 + 1
using namespace std;
int sum;

int p[MAX_V];
int r[MAX_V];

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

void Union(int x, int y, int w)
{
    x = find(x);
    y = find(y);
    if (x == y)
    {
        return;
    }

    if (r[x] > r[y])
    {
        p[y] = x;
        r[x] += r[y];
    }
    else
    {
        p[x] = y;
        r[y] += r[x];
    }
    sum += w;
}

int main()
{
    int v, e, a, b, c;
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
    scanf("%d %d", &v, &e);
    for (int i = 1; i <= e; i++)
    {
        scanf("%d %d %d", &a, &b, &c);
        pq.push({c, a, b});
    }

    for (int i = 1; i <= v; i++)
    {
        p[i] = i;
        r[i] = 1;
    }

    for (int i = 0; i < e; i++)
    {
        c = get<0>(pq.top());
        b = get<1>(pq.top());
        a = get<2>(pq.top());

        Union(a, b, c);
        pq.pop();
    }

    cout << sum;
}