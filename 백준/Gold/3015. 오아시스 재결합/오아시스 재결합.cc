#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

class people{  
    public:
    people(int h,int c){
        height=h;
        count = c;
    }
    int height;
    int count;
};

int main(){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    int n,h;
    long long pair=0;
    stack<people*>s;
    cin >> n;
    for (int i=0;i<n;i++){
        cin >> h;
        people *p = new people(h,1);

        while(!s.empty()){
            people *sp = s.top();
            if( p->height == sp->height){ // stack Top 사람이랑 같은경우
                pair+=sp->count;
                p->count+=sp->count;
            }
            else if(sp->height > h){ 
                pair++;
                break;
            }
            else{
                pair+=sp->count;
            }
            s.pop();
        }
        s.push(p);
    }
    cout << pair;
}