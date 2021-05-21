#include<stdio.h>
#include<stdlib.h>

// Chess board
int board[10000][10000];

int isItSafe(int i, int j, int N) {

	// Check any queen is present in the 
	// current column above the current cell 
	// if found to be true return false
	for (int r = 0; r < i; ++r) 
		if(board[r][j]) return 0;

	int r = i, c = j;

	// Check any queen is present in the upper 
	// left diagonal of the current cell if found 
	// to be true return false
	while(r>=0 && c>=0) {

		if(board[r][c]) return 0;
		r--; c--;
	}

	r = i, c = j; 
	// Check any queen is present in the upper 
	// right diagonal of the current cell if found 
	// to be true return false
	while(r>=0 && c<N) {

		if(board[r][c]) return 0;
		r--; c++;
	}

	// Otherwise current cell is safe 
	// return true
	return 1;
} 

void display(int N) {

	for(int i = 0; i < N; i++) {

		for (int j = 0; j < N; ++j) {

			printf("%d ", board[i][j]);
		}
		printf("\n");
	}
	printf("\n\n");
}

int nQueens(int N, int r) {

	// If all the queens are placed in all 
	// the rows return true
	if(r == N) return 1;

	// Traversing through the columns
	for(int c = 0; c < N; c++) {

		// Check current cell is safe 
		if(isItSafe(r, c, N)) {

			// Place the queen if the cell is safe
			board[r][c] = 1;

			// Recursion call for the next row
			if(nQueens(N, r+1)) return 1;

			// Backtracking step
			board[r][c] = 0;
		}
	}

	// If queen cannot be placed in the 
	// current row or cell return false
	return 0;
}

int main() {

	while(1) {

		int ch;
		printf("1.Enter the value of N:\n2.Exit the program\nEnter the choice: ");
		scanf("%d", &ch);
		if(ch == 1){
			int N;
			scanf("%d", &N);
			for(int i = 0; i < N; i++) 
				for (int j = 0; j < N; ++j) 
					board[i][j] = 0;
		
			if(nQueens(N, 0)) display(N);
		}
		else if(ch == 2) break;
		else printf("Invalid choice!\n");
	}

	return 0;
}
