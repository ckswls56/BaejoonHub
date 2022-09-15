#include <stdio.h>
#define max(a,b) (((a) > (b)) ? (a) : (b))

int mem[101];
int cost[101];
int dp[10001];

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &mem[i]);
	}

	for (int i = 1; i <= n; i++) {
		scanf("%d", &cost[i]);
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 10000; j >= cost[i]; j--) {
			dp[j] = max(dp[j], dp[j - cost[i]] + mem[i]);
		}
	}
    
    for(int i=0;i<=10000;i++){
        if(dp[i]>=m){
            printf("%d",i);
            break;
        }
    }
	return 0;
}