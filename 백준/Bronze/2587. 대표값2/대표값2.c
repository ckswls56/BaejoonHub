#include <stdio.h>

void swap(int *a,int *b){
    int temp = *a;
    *a=*b;
    *b=temp;
}

int main(){
    int arr[5];
    for(int i=0;i<5;i++){
        scanf("%d",&arr[i]);
    }
    
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            if(arr[i]>arr[j]){
                swap(&arr[i],&arr[j]);
            }
        }
    }
    
    int sum = 0;
    for(int i=0;i<5;i++){
        sum+=arr[i];
    }
    printf("%d\n%d",sum/5,arr[2]);
}