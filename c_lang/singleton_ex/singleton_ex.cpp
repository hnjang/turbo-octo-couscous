#include <iostream>
#include <iterator>
#include <set>
#include <vector>
#include <initializer_list>

class C {
	std::set<int> s;

  public:
	static C &getInstance() {
		static C instance;
		return instance;
	}
	bool insert(int i) {
		std::pair<std::set<int>::iterator, bool> ret = s.insert(i);
		return ret.second;
	}
	bool has(int i) {
		return s.find(i) != s.end();
	}
	/* dump() is not essential */
	void dump() {
		std::cout << "dump: ";
		std::copy(s.begin(), s.end(),
				  std::ostream_iterator<int>(std::cout, " "));
		std::cout << "\n";
	}

  private:
	C() {}
	/* prevent to call C(C const &) */
	C(C const &);
	/* prevent to call operator=() */
	void operator=(C const &);
};

void foo(std::vector<int> &v) {
	C &c = C::getInstance();
	for (int i = 0; i < v.size(); i++) {
		c.insert(v[i]);
	}
}

void bar(std::vector<int> &v) {
	C &c = C::getInstance();
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i] << " " << (c.has(v[i]) ? "y " : "n ");
	}
	std::cout << "\n";
}

int main() {
	std::vector<int> x{1, 3, 5, 7};
	std::vector<int> y{1, 4};
	std::vector<int> z{3, 4, 10};
	C &c = C::getInstance();
	c.dump();

	foo(x);
	c.dump();
	bar(z);

	foo(y);
	c.dump();
	bar(z);
}
