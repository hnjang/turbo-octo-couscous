#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <sstream>
#include <string>
#include <array>


bool readfile(std::string &filename, std::string &out, int count) {
	out = std::string();
	std::ifstream ifs(filename);
	if (!ifs.is_open())
		return false;
	while (!ifs.eof()) {
		if (count == 0)
			return true;
		std::string t;
		ifs >> t;
		out += t + "\t";
		count--;
	}
	return true;
}

#define SUBSTR_BY_IDX(a)                                                       \
	buf.substr(s_idx[(a)-1] + 1, s_idx[(a)] - s_idx[(a)-1] - 1)

bool parse_proc(std::string &filename) {
	std::string buf;
	std::ifstream ifs(filename);
	if (!ifs.is_open())
		return false;
	getline(ifs, buf);

	size_t first_space = buf.find(' ');
	pid_t pid = stoi(buf.substr(0, first_space));
	size_t r_paren = buf.find(')');
	std::string comm = buf.substr(first_space + 2, r_paren - first_space - 2);

	const int s_idx_len = 30;
	std::array<std::string::size_type, s_idx_len> s_idx;
	s_idx[0] = buf.find(' ', r_paren + 2);
	std::cout << "(r_paren+2)/s_idx[0]: " << r_paren + 2 << "/" << s_idx[0] << "\n";
	for (int i = 1; i < s_idx_len; i++) {
		s_idx[i] = buf.find(' ', s_idx[i - 1] + 1);
	}
	/*
	std::copy(s_idx.begin(), s_idx.end(),
			  std::ostream_iterator<std::string::size_type>(std::cout, " "));
			  */
	pid_t ppid = stoi(buf.substr(s_idx[0], s_idx[1]));
	std::string state = buf.substr(r_paren + 2, s_idx[0] - (r_paren + 2));
	unsigned long vsize = stoul(SUBSTR_BY_IDX(20));
	unsigned long rss = stoul(SUBSTR_BY_IDX(21));
	std::cout << pid << "/" << comm << "/" << state << "/" << ppid << "/"
			  << vsize << "/" << rss << "\n";
	return true;
}

int main() {
	std::string filename = "/proc/1/stat";
	std::string out;
	//readfile(filename, out, 100);
	parse_proc(filename);
	std::cout << out;
}
