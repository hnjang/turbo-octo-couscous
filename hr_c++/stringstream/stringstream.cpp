#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    int t;
    char ch;
    stringstream ss(str);
    vector<int> v;
    while (!ss.eof()) {
        ss >> t >> ch;
		cout << t << "/" << ch << "\n";
        v.push_back(t);
    }
    return v;
}

int main() {
    string str;
    //cin >> str;
	getline(cin, str);
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    return 0;
}

