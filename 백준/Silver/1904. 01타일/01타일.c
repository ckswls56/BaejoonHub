#include <stdio.h>
#include <stdlib.h>

int tile(int n) {
	if (n <= 0)
		return 0;
	else if (n == 1)
		return 1;
	int *arr;
	arr = (int*)malloc(sizeof(int)*n);
	arr[0] = 1; arr[1]=2;
	
	

	for (int i = 2; i < n;i++) {
		arr[i] = (arr[i - 1] + arr[i-2])%15746;
	}

	return arr[n - 1];
}

int main() {
	int n;
	scanf("%d", &n);

	printf("%d", tile(n));

}