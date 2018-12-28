#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    vector<int> v;
    int t;
    for(int i=0; i<n; i++){
        cin >> t;
        v.push_back(t);
    }
    sort(v.begin(), v.end());
	/*
	cout << "sorting is done.\n";
	for (int i=0; i<v.size(); i++){
		cout << v[i] << " ";
	}
	cout << "\n";
	*/
    int q;
    cin >> q;
    int y;
    for (int i=0; i<q; i++){
        cin >> y;
        vector<int>::iterator lo = lower_bound(v.begin(), v.end(), y);
        cout << ((*lo == y) ? "Yes " : "No ");
        cout << (lo - v.begin() +1) <<"\n";
    }
    return 0;
}

