#include <iostream>
#include <utility>
#include <tuple>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <string>
#define MAX_V 100 + 1
using namespace std;

double sum;

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

void Union(int x, int y, double w)
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

double distance(pair<double, double> p1, pair<double, double> p2)
{
    double dis;

    dis = sqrt(pow(p1.first - p2.first, 2) + pow(p1.second - p2.second, 2));
    return dis;
}

string double_to_str(pair<double, double> p)
{
    string s = to_string(p.first) + to_string(p.second);
    return s;
}

int main()
{
    //크루스칼 알고리즘 (MST)
    int n, index;
    double a, b, c;
    priority_queue<tuple<double, pair<double, double>, pair<double, double>>, vector<tuple<double, pair<double, double>, pair<double, double>>>, greater<tuple<double, pair<double, double>, pair<double, double>>>> pq;
    vector<pair<double, double>> v;
    map<string, int> m;
    scanf("%d", &n);
    index = 0;
    for (int i = 1; i <= n; i++)
    {
        scanf("%lf %lf", &a, &b);
        string s = to_string(a) + to_string(b);
        m.insert({s, index++});
        v.push_back({a, b});
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
                continue;

            c = distance(v[i], v[j]);
            pq.push({c, v[i], v[j]});
        }
    }

    for (int i = 1; i <= n; i++)
    {
        p[i] = i;
        r[i] = 1;
    }

    while (pq.size())
    {
        c = get<0>(pq.top());
        auto iter = m.begin();
        iter = m.find(double_to_str(get<1>(pq.top())));
        b = iter->second;
        iter = m.find(double_to_str(get<2>(pq.top())));
        a = iter->second;

        Union(a, b, c);
        pq.pop();
    }
    printf("%.2lf", sum);
}