#include <iostream>
#include <vector>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <cctype>

using namespace std;

class element {
  public:
	string name;
	vector<string> attrs;
	vector<string> values;
	vector<element> children;

	element(vector<string> attrs, vector<string> values,
			vector<element> children)
		: attrs{attrs}, values{values}, children{children} {}
	element() {}
	void set_name(string name_ar) {
		// cout << "set_name: entry: " << name_ar <<endl;
		name = name_ar;
	}
	friend std::ostream &operator<<(std::ostream &out, const element &e) {
		out << "name: " << e.name << std::endl;
		out << "attrs: ";
		std::copy(e.attrs.begin(), e.attrs.end(),
				  std::ostream_iterator<string>(out, " "));
		out << std::endl << "values: ";
		std::copy(e.values.begin(), e.values.end(),
				  std::ostream_iterator<string>(out, " "));
		out << std::endl << "children { ";
		std::copy(e.children.begin(), e.children.end(),
				  std::ostream_iterator<element>(out, " "));
		out << " } END of children" << std::endl;
		return out;
	}
};

bool is_end_tag(string str) {
	if (str.at(0) == '/')
		return true;
	return false;
}

bool is_end_tag(string str, string tag_name) {
	string s;
	s = "/" + tag_name;
	return s == str;
}

bool is_start_tag(string str) { return !is_end_tag(str); }

bool is_valid(string str) {
	if (str.size() == 0)
		return false;
	if (str.at(0) == '<')
		return true;
	return false;
}

string get_tag_name(string str) {
	size_t n = str.find(' ');
	// cout << "get_tag_name: str:" <<str <<  "\tn=" << n <<endl;
	return str.substr(0, n);
}

element create_new_group(vector<string> &input, string first) {
	istringstream first_ss(first);
	vector<string> first_tokens{istream_iterator<string>{first_ss},
		istream_iterator<string>{}};
	vector<string> attrs;
	vector<string> values;
	/*
	cout << __LINE__ <<":create_new_group: entry: first_tokens.size(): " <<first_tokens.size()<<endl;
	copy(first_tokens.begin(), first_tokens.end(), std::ostream_iterator<string>(cout, " "));
	cout << __LINE__ <<endl;
	*/
	for(int i=1; first_tokens.size() >= (i+3); i+=3) {
		attrs.push_back(first_tokens[i]);
		values.push_back(first_tokens[i+2]);
	}
	string tag_name;
	vector<element> children;
	while (input.size() > 0) {
		string buf = input[0];
		buf = buf.substr(1, buf.size()-2);
		//cout << "buf: " << buf << endl;
		input.erase(input.begin());
		if (is_start_tag(buf)) {
			tag_name = get_tag_name(buf);
			//cout << "\n\ntag: " << tag_name << endl;
			element c = create_new_group(input, buf);
			c.set_name(tag_name);
			children.push_back(c);
		} else {
			//cout << "this must be a end tag : " << buf << endl;
			if (is_end_tag(buf, tag_name))
				break;
		}
	}
	element res(attrs, values, children);
	return res;
}

vector<string> split(string str, string delim) {
	auto start = 0U;
	auto end = str.find(delim);
	vector<string> res;
	/*
	cout << __LINE__ << " str: " << str << " delim: " << delim
		 << " end: " << end << endl;
		 */
	while (end != string::npos) {
		res.push_back(str.substr(start, end - start));
		start = end + delim.length();
		end = str.find(delim, start);
	}
	res.push_back(str.substr(start, end));
	/*
		cout << __LINE__ <<endl;
	copy(res.begin(), res.end(), std::ostream_iterator<string>(cout, " "));
	cout << endl;
	*/
	return res;
}

void process_query(vector<string> &t, element &e) {
	//cout << __LINE__ <<" process_query: entry: t.size(): "<<t.size()<<endl;
	if (t.size()<=0) {
		//cout << __LINE__ <<endl;
		cout << "Not Found!" << endl;
	} else if (t.size()==1) {
		auto it = find(e.attrs.begin(), e.attrs.end(), t[0]);
		if (it==e.attrs.end()) {
			cout << "Not Found!" << endl;
			/*
			cout << __LINE__ <<endl;
			cout << "debug info: t[0]:" << t[0] << endl;
			copy(e.attrs.begin(), e.attrs.end(), std::ostream_iterator<string>(cout, " "));
			*/
		} else {
			string value = e.values[it - e.attrs.begin()];
			value = value.substr(1, value.size()-2);
			cout << value << endl;
		}
	} else {
		int i;
		for (i=0; i<e.children.size(); i++) {
			if (e.children[i].name == t[0]){
				t.erase(t.begin());
				process_query(t, e.children[i]);
				break;
			}
		}
		if (i==e.children.size()) {
			//cout << __LINE__ <<endl;
			cout << "Not Found!" << endl;
		}
	}
}

int main() {
	int n, q;
	cin >> n >> q;

	element root;
	root.set_name("root");
	vector<string> input;
	while (n--) {
		string buf;
		getline(cin, buf);

		if (!is_valid(buf)) {
			n++;
			continue;
		}
		input.push_back(buf);
		//cout << buf << endl;
	}
	vector<string> query;
	while (q--) {
		string buf;
		getline(cin, buf);
		query.push_back(buf);
		//cout << buf << endl;
	}

	string tag_name;
	while (input.size() > 0) {
		string buf = input[0];
		buf = buf.substr(1, buf.size()-2);
		//cout << "buf: " << buf << endl;
		input.erase(input.begin());
		if (is_start_tag(buf)) {
			tag_name = get_tag_name(buf);
			element c = create_new_group(input, buf);
			c.set_name(tag_name);
			root.children.push_back(c);
		} else {
			//cout << "this must be a end tag : " << buf << endl;
			if (is_end_tag(buf, tag_name))
				break;
		}
	}

	cout << "\nStart dumping... " <<endl;
	cout << root;
	for (int i=0; i<query.size(); i++) {
		vector<string> t = split(query[i], ".");
		vector<string> tt = split(t.back(), "~");
		t.pop_back();
		t.insert(t.end(), tt.begin(), tt.end());
		process_query(t, root);

	}
}
