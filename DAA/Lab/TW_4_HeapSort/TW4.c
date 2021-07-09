#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 10000
void getdata(int arr[])
{
 int i;
  //generating random numbers
  for(i=0;i<MAX;i++)
  {
     arr[i]=rand();
    }
} 

void heap_bottom_up(int n,int a[])
{
	int i,j,p,k,v,heap;
	p = n/2;
	
	for(i=p;i>0;i--)
	{
		heap = 0;
		k = i;
		v = a[k];
		
		while(!heap&&((2*k)<=n))
		{
			j = 2*k;
			if(j<n)
			{
				if(a[j]<a[j+1])
					j = j+1;
			}
			if(v>=a[j])
				heap = 1;
			else
			{
				a[k] = a[j];
				k = j;
			}
		}
		a[k] = v;
	}
}

void heapsort(int n,int a[])
{
	int i,temp;
	heap_bottom_up(n,a);
	for(i=n;i>1;i--)
	{
		temp = a[1];
		a[1] = a[i];
		a[i] = temp;
		heap_bottom_up(i-1,a);
	}
}

int main()
{
	int i,a[MAX],j,n;
	clock_t start,end;
	double duration;
	//printf("ENTER THE SIZE OF ARRAY : ");
	//scanf("%d",&n);
	
	//printf("ENTER %d ELEMENTS - \n",n);
	//for(i=1;i<=n;i++)
	//	scanf("%d",&a[i]);
	getdata(a);	
	clock_t t;
    t = clock();
    heapsort(MAX,a);
    t = clock() - t;
    double time_taken = ((double)t) / CLOCKS_PER_SEC; // in seconds
    printf("fun() took %f seconds to execute \n", time_taken);
	return 0;
}