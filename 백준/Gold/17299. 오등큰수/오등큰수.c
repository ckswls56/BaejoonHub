#include <stdio.h>
#include <stdlib.h>

int stack[1000001];
int arr[1000001];
int f[1000001];
int top = -1;

void push(int c)
{
    stack[++top] = c;
}

int pop()
{
    if (top != -1)
        return stack[top--];
    else
        return -1;
}

int get_top()
{
    if (top != -1)
        return stack[top];
    else
        return -1;
}

int find(int c)
{
    for (int i = top; i >= 0; i--)
    {
        if (f[stack[i]] > f[c])
            return stack[i];
    }
    return c;
}

int main()
{
    int n, x;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        f[arr[i]]++;
    }

    push(arr[n - 1]);
    int max = f[arr[n - 1]];
    for (int i = n - 2; i >= 0; i--)
    {
        if (max < f[arr[i]])
            max = f[arr[i]];

        if (f[arr[i]] < f[arr[i + 1]])
        {
            push(arr[i + 1]);
        }
        else if (f[arr[i]] == f[arr[i + 1]])
            push(get_top());
        else
        {
            if (f[arr[i]] < f[get_top()])
                push(get_top());
            else
            {
                if (max == f[arr[i]])
                    push(arr[i]);
                else
                {
                    push(find(arr[i]));
                }
            }
        }
    }

    int ngf;
    for (int i = 0; i < n; i++)
    {
        ngf = pop();
        if (arr[i] == ngf || f[arr[i]] == f[ngf])
        {
            printf("-1 ");
        }
        else
            printf("%d ", ngf);
    }
}