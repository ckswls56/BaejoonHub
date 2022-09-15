#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void bino(int **arr, int n) {

	for (int i = 0; i <= n; i++) //left line insert 1
		arr[i][0] = 1;
	for (int i = 0; i <= n; i++) //right line insert 1
		arr[i][i] = 1;

	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <i; j++) {
			arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j]);
		}
	}

}

void swap(char *a, char *b) {
	char  temp[30];
	strcpy(temp,a);
	strcpy(a, b);
	strcpy(b, temp);
}

int bubblesort(char **arr, int n) {
	int i, j;
	i = 0;
	while (i < n) {
		j = i;
		while (j < n) {
			if (strcmp(arr[i] , arr[j])>0)
				swap(arr[i], arr[j]);
			j++;
		}
		i++;
	}
	return 0;
}

int main() {

	int t,n,res;
	char temp[30];
	scanf("%d", &t);

	while (t-- > 0) {

		scanf("%d", &n);
		char **clothes;
		int count[30] = { 0 }; // clothes type
		clothes = (char**)malloc(sizeof(char*)*n);
		for (int i = 0; i < n; i++) {
			clothes[i] = (char*)malloc(21);
			scanf("%s", temp);
			scanf("%s", clothes[i]);
		}
		bubblesort(clothes, n);
		int j = 0;
		for (int i = 0; i < n-1; i++) {
			count[j]+=1;

			if (strcmp(clothes[i], clothes[i + 1]) != 0) {
				j++;
			}
		}
		count[j]++;

		/*int **arr;

		arr = (int**)malloc(sizeof(int*)*(n + 1));
		for (int i = 0; i <= n; i++) {
			arr[i] = (int*)malloc(sizeof(int)*(i + 1));
		}

		bino(arr, n);*/


	
		if (j == 0)
			res = ++n;
		else {
			res = 0;
			int temp = 1;
			for (int i = 0; i <= j; i++) {
				temp *= (count[i] + 1);
			}
			res = temp;
		}
		

		printf("%d\n", --res);
		//free(arr);
		free(clothes);
	}
	
	return 0;
}
