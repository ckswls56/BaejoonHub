#include <iostream>
#include <utility>
#include <tuple>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#define MAX_V 100 + 1

using namespace std;
int sum, n, m, index, e;

const int directon[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
char arr[MAX_V][MAX_V];
char visited[MAX_V][MAX_V];
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
    e++;
}

void bfs(int i, int j)
{
    index++;
    queue<pair<int, int>> q;
    q.push({i, j});
    visited[i][j] = index;

    while (q.size())
    {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int dy = directon[i][0];
            int dx = directon[i][1];
            if (x + dx >= 0 && y + dy >= 0 && x + dx < m && y + dy < n && visited[y + dy][x + dx] == 0 && arr[y + dy][x + dx])
            {
                visited[y + dy][x + dx] = index;
                q.push({y + dy, x + dx});
            }
        }
    }
}

int main()
{
    //크루스칼 알고리즘 (MST)
    int a, b, c;
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    index = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (arr[i][j] && !visited[i][j])
            {
                bfs(i, j);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (arr[i][j])
            {
                for (int k = 0; k < 4; k++)
                {
                    int dy = directon[k][0];
                    int dx = directon[k][1];
                    int cnt = 0;
                    switch (k)
                    {
                    case 0: // up
                        while (i + dy > 0 && !arr[i + dy][j])
                        {
                            cnt++;
                            dy--;
                        }
                        if (cnt >= 2 && arr[i + dy][j] && visited[i][j] != visited[i + dy][j])
                        {
                            pq.push({cnt, visited[i][j], visited[i + dy][j]});
                        }
                        break;
                    case 1: // down
                        while (i + dy < n - 1 && !arr[i + dy][j])
                        {
                            cnt++;
                            dy++;
                        }
                        if (cnt >= 2 && arr[i + dy][j] && visited[i][j] != visited[i + dy][j])
                        {
                            pq.push({cnt, visited[i][j], visited[i + dy][j]});
                        }
                        break;
                    case 2: // left
                        while (j + dx > 0 && !arr[i][j + dx])
                        {
                            cnt++;
                            dx--;
                        }
                        if (cnt >= 2 && arr[i][j + dx] && visited[i][j] != visited[i][j + dx])
                        {
                            pq.push({cnt, visited[i][j], visited[i][j + dx]});
                        }
                        break;
                    case 3: // right
                        while (j + dx < m - 1 && !arr[i][j + dx])
                        {
                            cnt++;
                            dx++;
                        }
                        if (cnt >= 2 && arr[i][j + dx] && visited[i][j] != visited[i][j + dx])
                        {
                            pq.push({cnt, visited[i][j], visited[i][j + dx]});
                        }
                        break;
                    }
                }
            }
        }
    }

    // bfs로 섬의 위치 정보를 다 확인후
    //완전탐색으로 섬과 섬의 모든 연결다리를 push한다 이후 크루스칼알고리즘으로 mst를 만든다.

    for (int i = 1; i <= n; i++)
    {
        p[i] = i;
        r[i] = 1;
    }

    while (pq.size())
    {
        c = get<0>(pq.top());
        b = get<1>(pq.top());
        a = get<2>(pq.top());

        Union(a, b, c);
        pq.pop();
    }

    if (e == index - 1)
        cout << sum;
    else
        cout << -1;
}