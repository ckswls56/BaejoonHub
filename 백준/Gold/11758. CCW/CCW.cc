#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
typedef pair<double, double>P;

int ccw(double x1, double x2, double x3, double y1, double y2, double y3) {
	double res = x1 * y2 + x2 * y3 + x3 * y1;
	res += (-y1 * x2 - y2 * x3 - y3 * x1);
	if(res<0)
        return -1;
    else if (res == 0)
        return 0;
    else
        return 1;
}

int main() {
	vector<P>arr(3);

	for (int i = 0; i < 3; i++)
		scanf("%lf%lf", &arr[i].first, &arr[i].second);
    
    printf("%d",ccw(arr[0].first,arr[1].first,arr[2].first,arr[0].second,arr[1].second,arr[2].second));
	return 0;
}