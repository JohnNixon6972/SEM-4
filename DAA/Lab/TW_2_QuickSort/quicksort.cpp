#include <iostream>
#include <time.h>
#include <stdio.h>
#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;

#define MAX 10000
void getdata(int array[])
{
    int i;
    //generating random numbers
    for (i = 0; i < MAX; i++)
    {
        array[i] = rand();
    }
}

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int array[], int beg, int end)
{
    int pivot = array[end];
    int i = beg - 1;

    for (int j = beg; j <= end - 1; j++)
    {
        if (array[j] < pivot)
        {
            i++;
            swap(&array[i], &array[j]);
        }
    }
    swap(&array[i + 1], &array[end]);
    return i + 1;
}

void quickSort(int array[], int beg, int end)
{
    if (beg < end)
    {
        int pivot_index = partition(array, beg, end);

        quickSort(array, beg, pivot_index-1);
        quickSort(array, pivot_index+1,end);

    }
}

int main(){
    int array[MAX];
    getdata(array);
    clock_t start, end;

    /* Recording the starting clock tick.*/
    start = clock();

    quickSort(array, 0,MAX-1);

    // Recording the end clock tick.
    end = clock();

    // Calculating total time taken by the program.
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed
         << time_taken << setprecision(5);
    cout << " sec " << endl;
    return 0;
}
