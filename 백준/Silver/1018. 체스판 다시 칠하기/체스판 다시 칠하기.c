#include <stdio.h>
#include <stdlib.h>

int chess(char **board) {
	int i = 0;
	int j = 0;
	int repaint = 0;
	int top=1;

	while (i < 8) {
		j = 0; top *= -1;
		while (j < 8) {
			if (top == 1) {
				if (board[i][j] == 'W')
					repaint++;
			}
			else {
				if (board[i][j] == 'B')
					repaint++;
			}
			top *= -1;
			j++;
		}
		i++;
	}
	return repaint;
}
int chess2(char **board) {
	int i = 0;
	int j = 0;
	int repaint = 0;
	int top = -1;

	while (i < 8) {
		j = 0; top *= -1;
		while (j < 8) {
			if (top == 1) {
				if (board[i][j] == 'W')
					repaint++;
			}
			else {
				if (board[i][j] == 'B')
					repaint++;
			}
			top *= -1;
			j++;
		}
		i++;
	}
	return repaint;
}

char **make_board(char **board, int n,int m) {
	int i, j;
	i = 0;
	char **res;
	res = (char**)malloc(sizeof(char*) * 8);

	while (i < 8) {
		j = 0;
		res[i] = (char*)malloc(sizeof(char)*9);
		while (j < 8) {
			res[i][j] = board[n][m];
			m++; j++;
		}
		n++; i++; m -= 8;
	}
	return res;
}

int main(){
	int n,m,i,j,min;
	scanf("%d %d", &n, &m);
	char ** board;
	char ** temp;
	int c1, c2;
	board = (char**)malloc(sizeof(char*)*n);
	i = 0;
	while (i < n) {
		board[i] = (char*)malloc(sizeof(char)*m + 1);
		scanf("%s", board[i++]);
	}
	i = 0; min = 1000000;

	while (i <= n - 8) {
		j = 0;
		while (j <= m - 8) {
			temp = make_board(board, i, j);
			c1 = chess(temp); c2 = chess2(temp);
			if (c1 < min || c2 < min) {
				if (c1 > c2)
					min = c2;
				else
					min = c1;
			}
			j++;
		}
		i++;
	}
	printf("%d", min);
	return 0;
}