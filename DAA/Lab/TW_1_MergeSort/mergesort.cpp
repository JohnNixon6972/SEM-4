#include <iostream>
#include <time.h>
#include <stdio.h>
#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;

#define MAX 2000
void getdata(int array[])
{
    int i;
    //generating random numbers
    for (i = 0; i < MAX; i++)
    {
        array[i] = rand();
    }
}

void merge(int array[], int low, int mid, int high)
{
    int left = (mid - low) + 1;
    int right = high - mid;

    int left_sub[left], right_sub[right];

    for (int i = 0; i < left; i++)
        left_sub[i] = array[left + i];
    for (int j = 0; j < right; j++)
        right_sub[j] = array[mid + 1 + j];

    int i = 0;
    int j = 0;
    int k = low;

    while (i < left && j < right)
    {
        if (left_sub[i] <= right_sub[j])
        {
            array[k] = left_sub[i];
            i++;
        }
        else
        {
            array[k] = right_sub[j];
            j++;
        }
        k++;
    }

    while (i < left)
    {
        array[k] = left_sub[i];
        i++;
        k++;
    }

    while (j < right)
    {
        array[k] = right_sub[j];
        j++;
        k++;
    }
}

void mergeSort(int array[], int low, int high)
{
    if (low >= high)
    {
        return;
    }
    int mid = (low + high) / 2;
    mergeSort(array, low, mid);
    mergeSort(array, mid + 1, high);
    merge(array, low, mid, high);
}

void printArray(int array[], int size)
{
    for (int i = 0; i < size; i++)
        cout << array[i] << " ";
}

int main()
{
    int array[MAX];
    int n, i;
    getdata(array);
    clock_t start, end;

    /* Recording the starting clock tick.*/
    start = clock();

    mergeSort(array, 0, MAX - 1);

    // Recording the end clock tick.
    end = clock();

    // Calculating total time taken by the program.
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed
         << time_taken << setprecision(6);
    cout << " sec " << endl;
    return 0;
}