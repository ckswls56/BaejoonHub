#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> coumputeSP(string p){
    int m = (int)p.size(), j=0;
    vector<int> sp(m, 0);
    for(int i = 1; i< m ; i++){
        while(j > 0 && p[i] !=  p[j])
            j = sp[j-1];
        if(p[i] == p[j])
            sp[i] = ++j;
    }
    return sp;
}
vector<int> kmp(string s, string p){
    vector<int> ans;
    auto sp = coumputeSP(p);
    int n = (int)s.size(), m = (int)p.size(), j =0;
    for(int i = 0 ; i < n ; i++){
        while(j>0 && s[i] != p[j])
            j = sp[j-1];
        if(s[i] == p[j]){
            if(j==m-1){
                ans.push_back(i-m+1);
                j = sp[j];
            }else{
                j++;
            }
        }
    }
    return ans;
}
int main(){
    string s, p;
    getline(cin, s);
    getline(cin, p);
    auto matched = kmp(s,p);
    printf("%d\n", (int)matched.size());
    for(auto i : matched)
        printf("%d ", i+1);
    return 0;
}