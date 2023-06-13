#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int i;
    cin >> i;
    while (i--)
    {
        string s;
        cin >> s;
        cout << s[0] << s.back() << "\n";
    }
}