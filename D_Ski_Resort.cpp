#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<queue>
#include<stack>
#include<unordered_map>
#include <math.h>
#include <climits>
#include <list>
#include <map>
#include <set>
#include <utility>
#define ll long long
#define mod 10000007
using namespace std;
 
#define int int64_t
#define vi vector<int>
#define vii vector<pair<int, int>>
#define vs vector<string>
#define vc vector<char>
#define vb vector<bool>
#define pb push_back
#define vvi vector<vector<int>>
#define pii pair<int, int>
#define umapii unordered_map<int,int>
#define umapci unordered_map<char,int>
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define loop(i, j, k) for (int i = j; i < k; i += 1)
#define rloop(i, j, k) for (int i = j; i >= k; i -= 1)
#define endl "\n"
#define inf (int)1e18
#define minf -9223372036854775807
#define PI 3.1415926535897932384626433832795
class customio{
    public:
    void operator>>(vi &arr){
        for (auto &x: arr) 
        cin >> x;
        return;
    }
    void operator<<(vi &arr){
        for (auto x: arr) 
        cout <<x<< " ";
    }
}vio;
#define cp(t) \
    int t;    \
    cin >> t; \
    while (t--)
  
signed main(){
    ios_base::sync_with_stdio(false);
    ios::sync_with_stdio(0);
    cout.tie(0);
    cin.tie(0);
    srand(time(NULL));
 
    cp(t){
        int n,k,q;
        cin>>n>>k>>q;
        vi arr(n);
        vio>>arr;
        int count=0;
        for(int i=0;i<n;){
            if(arr[i]>q){
                i++;
                continue;
            }
            int tcount=0;
            while((i<n)&&(arr[i]<=q)){
                i++;
                tcount++;
            }
            if(tcount>=k){
                int ab=(tcount-k)+1;
                count+=((ab+1)*ab)/2;
            }
        }
        cout<<count<<endl;
    }
}