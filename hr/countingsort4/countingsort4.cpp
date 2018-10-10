#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

class CS4Item {
public:
	int num;
	string str;
	int idx;
	CS4Item(int n, string s, int i) {
		num = n;
		str = s;
		idx = i;
	}
};

bool compare(CS4Item a, CS4Item b) {
	int num_diff = a.num - b.num;
	if (num_diff < 0) return true;
	else if (num_diff > 0) return false;
	else {
		int idx_diff = a.idx - b.idx;
		return (idx_diff < 0)? true : false;
	}
}

// Complete the countSort function below.
#if 0
void countSort(vector< vector<string> > arr) {
	int mid = arr.size() / 2;
	vector<CS4Item> v;
	for (int i=0; i<arr.size(); i++){
		int num = stoi(arr[i][0]);
		v.push_back(CS4Item(num, arr[i][1], i));
	}
	sort(v.begin(), v.end(), compare);
	for (int i=0; i<v.size(); i++){
		if (v[i].idx < mid)
			cout << "- ";
		else
			cout << v[i].str << " ";
	}

}
#else
void countSort(vector<CS4Item> v) {
	int mid = v.size() / 2;
	sort(v.begin(), v.end(), compare);
	for (int i=0; i<v.size(); i++){
		if (v[i].idx < mid)
			cout << "- ";
		else
			cout << v[i].str << " ";
	}

}

#endif

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

	vector<CS4Item> v;

    for (int i = 0; i < n; i++) {

        string arr_row_temp_temp;
        getline(cin, arr_row_temp_temp);

        vector<string> arr_row_temp = split(rtrim(arr_row_temp_temp));
		v.push_back(CS4Item(stoi(arr_row_temp[0]), arr_row_temp[1], i));
    }

    countSort(v);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
