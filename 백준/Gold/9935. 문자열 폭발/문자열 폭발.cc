#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
vector<char> v;
string str, bomb;

int main()
{
    cin >> str >> bomb;
    int str_size = str.size();
    int bomb_size = bomb.size();

    for (int i = 0; i < str_size; i++)
    {
        v.push_back(str[i]);

        if (v.size() >= bomb_size)
        {
            bool flag = true;

            for (int i = 0; i < bomb_size; i++)
            {
                if (v[v.size() - bomb_size + i] != bomb[i])
                {
                    flag = false; //폭탄 문자열이 아님
                    break;
                }
            }
            if (flag)
            {
                for (int i = 0; i < bomb_size; i++)
                    v.pop_back();
            }
        }
    }

    if (v.empty())
    {
        cout << "FRULA";
    }
    else
    {
        for (int i = 0; i < v.size(); i++)
        {
            cout << v[i];
        }
    }
}