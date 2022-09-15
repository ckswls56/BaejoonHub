#include <stdio.h>
#define MAX 101

typedef struct coordinate
{
    int x;
    int y;
    int z;
} coordinate;

const int direction[6][3] = {{1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, -1}, {0, 0, 1}};
char visited[MAX][MAX][MAX];
int res[MAX][MAX][MAX];
int arr[MAX][MAX][MAX];

coordinate q[MAX * MAX * MAX];
int front = -1;
int rear = -1;
int m, n, h;

void push(int y, int x, int z)
{
    q[++rear].y = y;
    q[rear].x = x;
    q[rear].z = z;
}

coordinate pop()
{
    return q[++front];
}

int size()
{
    return rear - front;
}

void bfs()
{
    coordinate c;

    while (size())
    {
        c = pop();
        int y = c.y;
        int x = c.x;
        int z = c.z;
        for (int i = 0; i < 6; i++)
        {
            int dz = direction[i][0];
            int dy = direction[i][1];
            int dx = direction[i][2];

            if ((y + dy >= 0 && y + dy < n) && (x + dx >= 0 && x + dx < m) && (z + dz >= 0 && z + dz < h) && arr[z + dz][y + dy][x + dx] == 0 && visited[z + dz][y + dy][x + dx] == 0)
            {
                res[z + dz][y + dy][x + dx] = res[z][y][x] + 1;
                push(y + dy, x + dx, z + dz);
                visited[z + dz][y + dy][x + dx] = 1;
            }
        }
    }
}

int check_box()
{
    int ret = 0;
    for (int k = 0; k < h; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {

                if (res[k][i][j] == 0 && arr[k][i][j] == 0)
                {
                    return -1;
                }
                else if (res[k][i][j] > ret)
                    ret = res[k][i][j];
            }
        }
    }

    return ret;
}

int main()
{
    scanf("%d %d %d", &m, &n, &h);
    for (int k = 0; k < h; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {

                scanf("%d", &arr[k][i][j]);
                if (arr[k][i][j] == 1)
                {
                    push(i, j, k);
                }
            }
        }
    }

    bfs();

    printf("%d", check_box());
}