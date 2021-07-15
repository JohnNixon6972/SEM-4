#include <stdio.h>
#include <stdlib.h>
#define MAX 20
int main(int argc, char *argv[])
{
    int weights[MAX], values[MAX], v[MAX][MAX], n, i, j, m, val1, val2, x[MAX];
    printf("ENTER THE NUMBER OF ITEMS : ");
    scanf("%d", &n);
    printf("ENTER WEIGHTS -\n");
    for (i = 1; i <= n; i++)
        scanf("%d", &weights[i]);
    printf("ENTER VALUES -\n");
    for (i = 1; i <= n; i++)
        scanf("%d", &values[i]);
    printf("ENTER THE KNAPSACK CAPACITY : ");
    scanf("%d", &m);
    for (i = 0; i <= n; i++)
    {
        for (j = 0; j <= m; j++)
        {
            if (i == 0 || j == 0)
                v[i][j] = 0;
            else
                v[i][j] = -1;
        }
    }
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= m; j++)
        {
            if (j < weights[i])
                v[i][j] = v[i - 1][j];
            else
            {
                val1 = values[i] + v[i - 1][j - weights[i]];
                val2 = v[i - 1][j];
                if (val1 > val2)
                    v[i][j] = val1;
                else
                    v[i][j] = val2;
            }
        }
    }
    printf("THE MATRIX IS....\n");
    for (i = 0; i <= n; i++)
    {
        for (j = 0; j <= m; j++)
        {
            printf("%d\t", v[i][j]);
        }
        printf("\n");
    }
    printf("MAXIMUM PR0FIT OBTAINED IS : %d\n", v[n][m]);
    i = n;
    j = m;
    while (i != 0 && j != 0)
    {
        if (v[i][j] != v[i - 1][j])
        {
            x[i] = 1;
            j = j - weights[i];
        }
        i = i - 1;
    }
    printf("ITEM SELECTED ARE --\n");
    printf("{");
    for (i = 0; i <= n; i++)
    {
        if (x[i] == 1)
            printf(" %d ", i);
    }
    printf("}\n");
    // system("PAUSE");
    return 0;
}