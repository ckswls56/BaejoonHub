#include <iostream>
using namespace std;
int chessB[2001][2001];
int chessW[2001][2001];

int main()
{
    int n, m, k;

    cin >> n >> m >> k;
    char c;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> c;
            chessB[i][j] = chessB[i - 1][j] + chessB[i][j - 1] - chessB[i - 1][j - 1];
            chessW[i][j] = chessW[i - 1][j] + chessW[i][j - 1] - chessW[i - 1][j - 1];
            if (((i % 2 == 1 && j % 2 == 0) || (i % 2 == 0 && j % 2 == 1)))
            {
                if (c == 'B')
                    chessB[i][j]++;
            }
            else if (c == 'W')
                chessB[i][j]++;

            if (((i % 2 == 0 && j % 2 == 0) || (i % 2 == 1 && j % 2 == 1)))
            {
                if (c != 'W')
                    chessW[i][j]++;
            }
            else if (c == 'W')
                chessW[i][j]++;
        }
    }


    int minB = 987564321;
    int minW = 987654321;

    for (int i = n; i >= k; i--)
    {
        for (int j = m; j >= k; j--)
        {
            if (chessB[i][j] - chessB[i - k][j] - chessB[i][j - k] + chessB[i - k][j - k] < minB)
                minB = chessB[i][j] - chessB[i - k][j] - chessB[i][j - k] + chessB[i - k][j - k];
        }
    }

    for (int i = n; i >= k; i--)
    {
        for (int j = m; j >= k; j--)
        {
            if (chessW[i][j] - chessW[i - k][j] - chessW[i][j - k] + chessW[i - k][j - k] < minW)
                minW = chessW[i][j] - chessW[i - k][j] - chessW[i][j - k] + chessW[i - k][j - k];
        }
    }

    if (minB < minW)
        cout << minB;
    else
        cout << minW;
}