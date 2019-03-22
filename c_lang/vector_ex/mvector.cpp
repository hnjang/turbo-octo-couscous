#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <stdio.h>
#include "common.h"
#include "mvector.h"

// every printf() is just a test code

//using namespace std;
using std::string;
using std::vector;

class element {
	long long id;
	string name;
	int bmi; // body mass index
	int max_bmi;
public:
	element(long long id, string name, int bmi) :
		id{id}, name{name}, bmi{bmi}, max_bmi{bmi} {}
	void update_max_bmi(const element &b) {
		max_bmi = std::max(max_bmi, b.max_bmi);
	}
	bool is_smaller_max_bmi_than(const element &b) const {
		return max_bmi < b.max_bmi;
	}
	string str() {
		std::ostringstream ss;
		ss << "id/name bmi(max) : " << id << '/' << name
			<< ' ' << bmi << '(' << max_bmi << ")";
		return ss.str();
	}
	bool operator<(const element &b) const { return id < b.id; }
	bool operator>(const element &b) const { return id > b.id; }
	bool operator==(const element &b) const {
		return id == b.id && name == b.name;
	}
};

// g_list is sorted list.
static vector<element> g_list;

int arr2vector(struct item * arr, int size, vector<element> &v) {
	for(int i=0; i<size; i++){
		element e {arr[i].id, string(arr[i].name), arr[i].bmi};
		v.push_back(e);
	}
}

int find_element(element &e) {
	int l = 0;
	int r = g_list.size() - 1;
	int m;
	while (l<=r) {
		m = l + (r-l) / 2;
		if (g_list[m] == e) {
			return m;
		}
		if (g_list[m] < e)
			l = m + 1;
		else
			r = m - 1;
	}
	return -1;
}

int print_list(vector<element> &v) {
	printf("%s:%d\n",__func__,__LINE__);
	for(int i=0; i<v.size(); i++){
		printf("%s\n", v[i].str().c_str());
	}
}

int update_list(struct item * arr, int size) {
	vector<element> v;
	vector<element> new_items;
	arr2vector(arr, size, v);

	std::sort(v.begin(), v.end());
	if (!g_list.empty()) {
		for (int i=0; i<v.size(); i++) {
			int f = find_element(v[i]);
			if (f<0) continue;
			if (g_list[f].is_smaller_max_bmi_than(v[i])){
				printf("max_bmi will be increased!\n");
				printf("old data: %s\n", g_list[f].str().c_str());
				printf("new data: %s\n", v[i].str().c_str());
			}
			v[i].update_max_bmi(g_list[f]);
		}
	}
	std::swap(v, g_list);
	print_list(g_list);
}

// update_list_v2() do below works.
// - if a element exists in v and in g_list, print old data and new data
//	and update max_bmi of the element of v
// - finally, swap v with g_list
//
// this function have to maintain g_list and can be called repeatedly.
void update_list_v2(vector<element> &v) {
	std::sort(v.begin(), v.end());
	if (!g_list.empty()) {
		for (int i=0; i<v.size(); i++) {
			int f = find_element(v[i]);
			if (f<0) continue;
			if (g_list[f].is_smaller_max_bmi_than(v[i])){
				printf("max_bmi will be increased!\n");
				printf("old data: %s\n", g_list[f].str().c_str());
				printf("new data: %s\n", v[i].str().c_str());
			}
			v[i].update_max_bmi(g_list[f]);
		}
	}
	std::swap(v, g_list);
	// abort();
}

#ifdef USE_MV_MAIN
int main(int argc, const char *argv[])
{
	printf("run main() of mvector.cpp\n");
	vector<element> a {
		{ 12, "a", 12 },
		{ 11, "b", 11 },
		{ 13, "c", 13 },
		{ 5, "d", 5 },
		{ 6, "e", 6 },
		{ 7, "f", 7 },
	};
	update_list_v2(a);
	//std::copy(g_list.begin(), g_list.end(), std::ostream_iterator<element>{std::cout});
	print_list(g_list);

	vector<element> b {
		{ 12, "a", 20 },
		{ 1, "x", 5 },
		{ 13, "c", 5 },
		{ 5, "d", 10 },
		{ 6, "e", 6 },
		{ 99, "y", 5 },
	};
	update_list_v2(b);
	//std::copy(g_list.begin(), g_list.end(), std::ostream_iterator<element>{std::cout});
	print_list(g_list);

	return 0;
}
#endif

