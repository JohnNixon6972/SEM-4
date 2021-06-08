# include <stdio.h>


	# define  INFINITY  9999
	# define  TRUE   1
	# define  FALSE  0


	void InitGraph(int g[20][20], int n)
	{
	    int i,j;
	    for(i=1; i<=n; i++)
	    for(j=1; j<=n; j++)
          g[i][j] = INFINITY;

	}

	void ReadGraph(int g[20][20])
	{
	   int i, j, wt;int ch; 
	   do
	   {
	      printf("\n Input Directed Edge <v1, v2, Wt> : ");
	      scanf("%d%d%d", &i, &j, &wt);
	      g[i][j] = wt;
	      printf(" One More Edge then press 1 else type any key ");
	      scanf("%d",&ch);
	   }while(ch==1);
	}

	void PrintGraph(int a[20][20], int n)
	{
	    int i,j;
	    for(i=1; i<=n; i++)
	    {
	       for(j=1; j<=n; j++)
		  printf("%8d", a[i][j]);
	       printf("\n\n");
	    }
	}


	int MIN(int a, int b)
	{
	   return( (a<b)?a:b );
	}

	int MinNode(int dist[], int n, int selected[])
	{
	    int k, min=INFINITY, index=0;
	    for(k=1; k<=n; k++)
	      if( dist[k]<min && selected[k]==FALSE)
	       {  min = dist[k];   index=k; }
	    return(index);
	}

	void svspaths(int g[20][20], int n, int sv, int dist[])
	{
	    int selected[20], k,u,w;

	    for(k=1; k<=n; k++)
	    {
	       selected[k] = FALSE;
	       dist[k] = g[sv][k];
	    }

	    selected[sv]=TRUE;
	    dist[sv]=0;

	    for(k=1; k<=n-1; k++)
	    {
		u = MinNode(dist, n, selected);
		selected[u] = TRUE;
		for(w=1; w<=n; w++)
		   if( selected[w]==FALSE )
		      dist[w] = MIN( dist[w], dist[u]+g[u][w] );
	    }
	}

	void main()
	{
	   int n, g[20][20], sv, dist[20];
	   int k;
	   
	   printf("\n Enter How many nodes : ");
	   scanf("%d", &n);
	   InitGraph(g,n);
	   ReadGraph(g);
	  



 printf("\n Enter the Starting Vertex : ");
	   scanf("%d", &sv);
	   svspaths(g, n, sv, dist);
	   printf("\n\n The Given Graph in Matrix Format : \n\n");
	   PrintGraph(g,n);
	   getchar();

	   printf("\n Single Vertex Shortest Paths : \n");
	   for(k=1; k<=n; k++)
	      printf("\n From Node-%d to Node-%d : %d", sv, k, dist[k] );

	   getchar();
	}