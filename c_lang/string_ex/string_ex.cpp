#include <vector>
#include <cstdint>
#include <iostream>

class my_length {
	uint64_t v;		// unit is 'mm'
	bool fmt_auto;
	public:
	my_length (uint64_t v) : v{v}, fmt_auto(false) {}
	friend std::ostream &operator<<(std::ostream &out, const my_length &l) {
		if (!l.fmt_auto) {
			return out << l.v << "mm";
		} else {
			if (l.v<10)
				return out << l.v << "mm";
			else if (l.v<1000)
				return out << double(l.v)/10 << "cm";
			else if (l.v<1000000)
				return out << double(l.v)/1000 << "m";
			else
				return out << double(l.v)/1000000 << "km";
		}
	}
	void set_fmt_auto(bool b) {fmt_auto = b;}
};

bool need_fmt_auto(int x) {
	return (x%2) != 0;
}

int main() {
	std::vector<my_length> lengths;
	my_length l{1};
	lengths.push_back(l);
	uint64_t val = 17;
	for (int i=0; i<9; i++) {
		my_length l{val};
		lengths.push_back(l);
		val *= 10;
	}
	for (int i=0; i<lengths.size(); i++) {
		if (need_fmt_auto(i)) {
			lengths[i].set_fmt_auto(true);
			std::cout << "fmt_auto: ";
		}
		std::cout << lengths[i] << "\n";
	}
}
