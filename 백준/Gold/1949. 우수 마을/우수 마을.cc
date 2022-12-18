#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;
#define MAX 10000 + 1
vector<int> tree[MAX];
int cost[MAX];
int dp[MAX][2];

int sol(int current, int selected, int prev)
{
    int &ret = dp[current][selected];
    if (ret != -1)
        return ret;

    if (selected)
    {
        ret = cost[current];
        for (auto next : tree[current])
        {
            if (next != prev)
            {
                ret += sol(next, false, current);
            }
        }
    }
    else
    {
        ret = 0;
        for (auto next : tree[current])
        {
            if (next != prev)
            {
                ret += max(sol(next, true, current), sol(next, false, current));
            }
        }
    }

    return ret;
}

bool visit[MAX];
vector<int> path;

void dfs(int current, int prev)
{
    // 현재 집합을 독립집합에 포함하는것 이 포함하지 않는 경우보다 더 큰 독립 집합을 얻을 수 있음
    if (dp[current][true] > dp[current][false] && !visit[current])
    {
        visit[current] = true;
        path.push_back(current);
    }

    for (auto next : tree[current])
    {
        if (next != prev)
        {
            dfs(next, current);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> cost[i];
    }
    int a, b;
    for (int i = 1; i < n; i++)
    {
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    memset(dp, -1, sizeof(dp));

    cout << max(sol(1, true, 0), sol(1, false, 0)) << endl;

    // dfs(1, 0);
    // sort(path.begin(), path.end());
    // for (auto x : path)
    // {
    //     cout << x << " ";
    // }

    return 0;
}
