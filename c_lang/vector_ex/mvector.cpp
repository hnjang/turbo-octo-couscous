#include <vector>
#include <string>
#include <algorithm>
#include <stdio.h>
#include "common.h"
#include "mvector.h"

// every printf() is just a test code

using namespace std;

class element {
public:
	long long id;
	string name;
	int tail_length;
	int weight;
	bool remove;
	static bool is_lower_id(element a, element b) {
		return a.id < b.id;
	}
	static bool is_same(element a, element b) {
		return (a.id == b.id) &&
				(0 == a.name.compare(b.name));
	}
	static void print(element a) {
		printf("%lld/%s\n", a.id, a.name.c_str());
	}
};

// g_list is sorted list.
static vector<element> g_list;

int arr2vector(struct item * arr, int size, vector<element> &v) {
	for(int i=0; i<size; i++){
		element e;
		e.id = arr[i].id;
		e.name = string(arr[i].name);
		v.push_back(e);
	}
}

int find_element(element &e) {
	int l = 0;
	int r = g_list.size() - 1;
	int m;
	while (l<=r) {
		m = l + (r-l) / 2;
		if (element::is_same(g_list[m], e)){
			return m;
		}
		if (element::is_lower_id(g_list[m], e))
			l = m + 1;
		else
			r = m - 1;
	}
	return -1;
}

int print_list(vector<element> &v) {
	printf("%s:%d\n",__func__,__LINE__);
	for(int i=0; i<v.size(); i++){
		element::print(v[i]);
	}
}

int update_list(struct item * arr, int size) {
	vector<element> v;
	vector<element> new_items;
	arr2vector(arr, size, v);
	//sort(v.begin(), v.end(), element::is_lower_id);
	printf("%s:%d: print v\n",__func__,__LINE__);
	print_list(v);
	if (g_list.size() == 0) {
		sort(v.begin(), v.end(), element::is_lower_id);
		g_list = v;
		printf("%s:%d: sort() is done. now print g_list\n",__func__,__LINE__);
		print_list(g_list);
		return 0;
	}
	for (int i=0; i<g_list.size(); i++) {
		g_list[i].remove = true;
	}
	for (int i=0; i<v.size(); i++) {
		int f = find_element(v[i]);
		if (f>=0) {
			g_list[f].remove = false;
		} else {
			new_items.push_back(v[i]);
		}
	}
	// remove every element which 'remove' is true.
	for (vector<element>::iterator it = g_list.begin(); it != g_list.end(); ++it) {
		while (it != g_list.end()){
			if (it->remove) {
				printf("remove: size/it: %d/%d\n", g_list.size(), int(it - g_list.begin()));
				element::print(g_list[it - g_list.begin()]);
				g_list.erase(it);
			} else {
				break;
			}
		}
	}
	for (int i=0; i<new_items.size(); i++) {
		g_list.push_back(new_items[i]);
	}
	sort(g_list.begin(), g_list.end(), element::is_lower_id);
	printf("%s:%d: sort() is done. now print g_list\n",__func__,__LINE__);
	print_list(g_list);

}

// update_list_v2() do below works.
// - remove every element of g_list, if the element exists in v
// - add a element to g_list, if a element exists in v and does not exist in g_list.
// - if a element exists in v and in g_list, do something
//
// this function have to maintain g_list and can be called repeatedly.
int update_list_v2(vector<element> &v) {
	vector<element> new_items;
	if (g_list.size() == 0) {
		sort(v.begin(), v.end(), element::is_lower_id);
		g_list = v;
		return 0;
	}
	// initialize 'remove'
	for (int i=0; i<g_list.size(); i++) {
		g_list[i].remove = true;
	}
	for (int i=0; i<v.size(); i++) {
		int f = find_element(v[i]);
		if (f>=0) {
			g_list[f].remove = false;
			// do_something
		} else {
			new_items.push_back(v[i]);
		}
	}
	// remove every element which 'remove' is true.
	for (vector<element>::iterator it = g_list.begin(); it != g_list.end(); ) {
		if (it->remove) {
			g_list.erase(it);
		} else {
			++it;
		}
	}
	// now, merge new_items to g_list
	for (int i=0; i<new_items.size(); i++) {
		g_list.push_back(new_items[i]);
	}
	// finally, sort g_list
	sort(g_list.begin(), g_list.end(), element::is_lower_id);

}

#ifdef USE_MV_MAIN
int main(int argc, const char *argv[])
{
	int a_id[] = {12, 11, 13, 5, 6, 7};
	const char * a_name[] = {"a", "b", "c", "d", "e", "f"};
	int b_id[] = {12, 1, 13, 5, 6, 99};
	const char * b_name[] = {"a", "x", "c", "d", "e", "y"};
	vector<element> a, b;
	for(int i=0; i<6; i++){
		element x;
		x.id = a_id[i];
		x.name = string(a_name[i]);
		a.push_back(x);
	}
	update_list_v2(a);
	print_list(g_list);
	for(int i=0; i<6; i++){
		element x;
		x.id = b_id[i];
		x.name = string(b_name[i]);
		b.push_back(x);
	}
	update_list_v2(b);
	print_list(g_list);

	return 0;
}
#endif

