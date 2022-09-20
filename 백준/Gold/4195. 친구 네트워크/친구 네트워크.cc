#include <iostream>
#include <map>
#include <string>
#define MAX_SIZE 200000 + 1

using namespace std;

int p[MAX_SIZE]; //  부모
int r[MAX_SIZE];

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
}

int main()
{ //
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t, f, a, b, index;
    string id1, id2;
    map<string, int> m;
    cin >> t;

    while (t--)
    {
        m.clear();
        index = 0;
        cin >> f;

        for (int i = 0; i < MAX_SIZE; i++)
        {
            p[i] = i; // p[i]=i 인경우 root노드
            r[i] = 1;
        }

        for (int i = 0; i < f; i++)
        {
            cin >> id1 >> id2;
            //if (m.find(id1) == m.end())
                m.insert({id1, index++});
           //if (m.find(id2) == m.end())
                m.insert({id2, index++});
            int a = m.find(id1)->second;
            int b = m.find(id2)->second;
            Union(a, b);

            cout << r[find(a)] << '\n';
        }
    }
}