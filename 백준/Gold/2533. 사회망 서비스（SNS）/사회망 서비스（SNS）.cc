#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;
#define MAX 1000000 + 1
vector<int> tree[MAX];
int dp[MAX][2];

int sol(int current, int selected, int prev)
{
    int &ret = dp[current][selected];
    if (ret != -1)
        return ret;

    if (selected)
    {
        ret = 1;
        for (auto next : tree[current])
        {
            if (next != prev)
            {
                ret += min(sol(next, true, current), sol(next, false, current));
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
                ret += sol(next, true, current);
            }
        }
    }

    return ret;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;
    int a, b;
    for (int i = 1; i < n; i++)
    {
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    memset(dp, -1, sizeof(dp));
    cout << min(sol(1, true, 0), sol(1, false, 0)) << endl;
    return 0;
}
