#include <vector>
#include <array>
#include <string>
#include <cstdint>
#include <iostream>

class Length {
	struct Units {
		int limit;
		double divisor;
		std::string name;
	};
	static const std::array<Units, 4> units;
	int id;
	std::string name;
	uint64_t v; // unit is 'mm'
	bool fmt_auto;

  public:
	Length(int id, std::string name, uint64_t v)
		: id{id}, name{name}, v{v}, fmt_auto(false) {}
	const Units &selectUnit() const {
		// if fmt_auto, select units automatically.
		// otherwise, use default unit
		auto ret = units.begin();
		if (fmt_auto) {
			while (ret->limit && v >= ret->limit) {
				++ret;
			}
		}
		return *ret;
	}
	friend std::ostream &operator<<(std::ostream &out, const Length &l) {
		const Units u = l.selectUnit();
		return out << l.id << "" << l.name << " : " << l.v / u.divisor
				   << u.name;
	}

	void set_fmt_auto(bool b) { fmt_auto = b; }
};

const std::array<Length::Units, 4> Length::units {{
	{10, 1, "mm"},
	{1000, 10, "cm"},
	{1000000, 1000, "m"},
	{0, 1000000, "km"}
}};

bool need_fmt_auto(int x) {
	return (x % 2) != 0;
}

int main() {
	std::string test("a");
	std::vector<Length> lengths;
	Length l{0, std::string("a"), 1};
	lengths.push_back(l);
	uint64_t val = 17;
	for (int i = 1; i < 10; i++) {
		Length l{i, std::string(1, 'a' + i), val};
		lengths.push_back(l);
		val *= 10;
	}
	for (int i = 0; i < lengths.size(); i++) {
		if (need_fmt_auto(i)) {
			lengths[i].set_fmt_auto(true);
			std::cout << "fmt_auto: ";
		}
		std::cout << lengths[i] << "\n";
	}
}
