#include <iostream>
#include <utility>
#include <tuple>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#define MAX_V 100000 + 1
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
        return;

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
    // cout << sum << "\n";
}

int distance(tuple<int, int, int> p1, tuple<int, int, int> p2)
{
    int a = abs(get<0>(p1) - get<0>(p2));
    int b = abs(get<1>(p1) - get<1>(p2));
    int c = abs(get<2>(p1) - get<2>(p2));

    int dis = min(a, b);
    dis = min(dis, c);
    return dis;
}

bool comp_x(tuple<int, int, int> t1, tuple<int, int, int> t2)
{
    return get<0>(t1) < get<0>(t2);
}

bool comp_y(tuple<int, int, int> t1, tuple<int, int, int> t2)
{
    return get<1>(t1) < get<1>(t2);
}

bool comp_z(tuple<int, int, int> t1, tuple<int, int, int> t2)
{
    return get<2>(t1) < get<2>(t2);
}

int main()
{
    //크루스칼 알고리즘 (MST)
    int n, x, y, z, d, a, b;
    priority_queue<tuple<int, tuple<int, int, int>, tuple<int, int, int>>, vector<tuple<int, tuple<int, int, int>, tuple<int, int, int>>>, greater<tuple<int, tuple<int, int, int>, tuple<int, int, int>>>> pq;
    vector<tuple<int, int, int>> v;
    map<tuple<int, int, int>, int> map;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d %d %d", &x, &y, &z);
        v.push_back({x, y, z});
        map.insert({{x, y, z}, i});
    }

    for (int i = 1; i <= n; i++)
    {
        p[i] = i;
        r[i] = 1;
    }

    vector<tuple<int, int, int>> sorted_v[3];
    for (int i = 0; i < 3; i++)
        sorted_v[i] = v;
    sort(sorted_v[0].begin(), sorted_v[0].end(), comp_x);
    sort(sorted_v[1].begin(), sorted_v[1].end(), comp_y);
    sort(sorted_v[2].begin(), sorted_v[2].end(), comp_z);

    for (int i = 0; i < n - 1; i++)
    {
        pq.push({distance(sorted_v[0][i], sorted_v[0][i + 1]), sorted_v[0][i], sorted_v[0][i + 1]});
        pq.push({distance(sorted_v[1][i], sorted_v[1][i + 1]), sorted_v[1][i], sorted_v[1][i + 1]});
        pq.push({distance(sorted_v[2][i], sorted_v[2][i + 1]), sorted_v[2][i], sorted_v[2][i + 1]});
    }

    while (pq.size())
    {
        d = get<0>(pq.top());
        a = map.find(get<1>(pq.top()))->second;
        b = map.find(get<2>(pq.top()))->second;
        Union(a, b, d);
        pq.pop();
    }
    printf("%d", sum);
}