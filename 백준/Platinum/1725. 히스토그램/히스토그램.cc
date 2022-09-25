#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

int n, ans, h[100002];

int main()
{
    stack<int> s;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> h[i];
    }

    for (int i = 0; i <= n + 1; i++)
    {
        while (!s.empty() && h[s.top()] > h[i])
        {
            int top = s.top();
            s.pop();
            ans = max(ans, h[top] * (i - s.top() - 1));
        }
        s.push(i);
    }

    cout << ans;
}