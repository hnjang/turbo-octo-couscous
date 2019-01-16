#include <iostream>

using namespace std;

class MValue {
	int val;
	int max_v;
	unsigned cnt;
	public:
	MValue(int v) : val{v}, max_v{v}, cnt{0} {
		cout << "MValue(int v) is called. ";
		cout << v <<"\n";
	}
};

class MContainer {
	MValue mval;
	public:
	MContainer() : mval{0} {}
	void set_mval(int val_ar) {
		mval = val_ar;
	}
};

int main(){
	MContainer mc;
	mc.set_mval(100);
}
