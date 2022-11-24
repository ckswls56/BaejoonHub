#include <stdio.h>

int main(){
    int arr[31];
    for(int i=1;i<=30;i++)
       arr[i]=1;
    for(int i=0;i<28;i++){
        int x;
        scanf("%d",&x);
        arr[x]=0;
    }
    
    for(int i=1;i<=30;i++){
        if(arr[i])
            printf("%d\n",i);
    }
    
}