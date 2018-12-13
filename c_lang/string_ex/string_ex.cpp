#include <vector>
#include <string>
#include <cstdint>
#include <iostream>

class my_length {
	int id;
	std::string name;
	uint64_t v;		// unit is 'mm'
	bool fmt_auto;

	public:
	my_length (int id, std::string name, uint64_t v)
		: id{id}, name{name}, v{v}, fmt_auto(false) {}
	friend std::ostream &operator<<(std::ostream &out, const my_length &l) {
		out << l.id << "/" << l.name << " : ";
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
	my_length l{0, "a", 1};
	lengths.push_back(l);
	uint64_t val = 17;
	for (int i=1; i<10; i++) {
		my_length l{i, std::string(1, 'a'+i), val};
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
