#include <vector>
#include <string>
#include <cstdint>
#include <iostream>

enum ENUM_OUTPUT {
	OUT_CUSTOMER,
	OUT_CLERK,
	OUT_MAX_IDX
};

class product {
	int id;
	std::string name;
	std::string desc;
	std::string secret_note;
	int output_mode;

  public:
	product(int id, std::string name, std::string desc, std::string secret_note)
		: id{id}, name{name}, desc{desc}, secret_note{secret_note},
		  output_mode{OUT_CUSTOMER} {}
	friend std::ostream &operator<<(std::ostream &out, const product &obj) {
		out << "name: " << obj.name << "\tdescription: " << obj.desc;
		if (obj.output_mode == OUT_CUSTOMER)
			return out;
		return out << "\nid: " << std::hex << obj.id << std::dec
				   << "\tnote: " << obj.secret_note;
	}
	void set_output_mode(int mode) { output_mode = mode; }
};

#if 0
int next_output_mode() {
	static int m = -1;
	m = (m+1)%OUT_MAX_IDX;
	return m;
}
#endif

int main() {
	std::vector<product> prods{
		{0xc0, "black chair", "people can sit on it. best-selling chair",
		 "good chair"},
		{0xc1, "white chair", "people can sit on it", ""},
		{0x00, "blue notebook", "simple paper notebook", ""},
		{0x01, "green notebook",
		 "simple paper notebook. Special discount today", ""},
		{0x10, "purple optical mouse", "simple mouse. Special discount today",
		 "it has many complaints"},
		{0x11, "white optical mouse", "simple mouse.", ""},

	};
	for (int m = 0; m < OUT_MAX_IDX; m++) {
		std::cout << "\nmode: " << m << "\n";
		for (int i = 0; i < prods.size(); i++) {
			prods[i].set_output_mode(m);
			std::cout << prods[i] << "\n";
		}
	}
}
