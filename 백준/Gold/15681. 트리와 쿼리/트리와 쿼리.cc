#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 100000 + 1
vector<int> tree[MAX];

int p[MAX];         // 부모정보
vector<int> c[MAX]; // 자식정보
int res[MAX];

void makeTree(int currentNode, int parent)
{
    for (int i = 0; i < tree[currentNode].size(); i++)
    {
        int node = tree[currentNode][i];
        if (node != parent)
        {
            // add node to currentNode's child
            c[currentNode].push_back(node);
            // set node's parent to cureentNode
            p[node] = currentNode;
            makeTree(node, currentNode);
        }
    }
}

void countSubtreeNodes(int currentNode)
{
    res[currentNode] = 1;

    for (int i = 0; i < c[currentNode].size(); i++)
    {
        countSubtreeNodes(c[currentNode][i]);
        res[currentNode] += res[c[currentNode][i]];
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, r, q, a, b;
    cin >> n >> r >> q;
    for (int i = 1; i < n; i++)
    {
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    makeTree(r, -1);
    countSubtreeNodes(r);

    for (int i = 0; i < q; i++)
    {
        cin >> a;
        cout << res[a] << "\n";
    }
}
