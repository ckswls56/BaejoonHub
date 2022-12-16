#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    queue<int> q;

    int x;
    cin >> n;
    cin >> x;
    while (x != -1)
    {
        if (x == 0)
            q.pop();
        else if (q.size() != n)
        {
            q.push(x);
        }
        cin >> x;
    }

    if (q.empty())
        cout << "empty";
    else
    {
        while (!q.empty())
        {
            x = q.front();
            cout << x << " ";
            q.pop();
        }
    }
}