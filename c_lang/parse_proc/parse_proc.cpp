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

bool parse_proc(const std::string &filename) {
	std::string buf;
	std::ifstream ifs(filename);
	if (!ifs.is_open())
		return false;
	getline(ifs, buf);

	std::cout << buf << "\n";
	size_t second_token = buf.find(' ') + 1;
	pid_t pid = stoi(buf.substr(0, second_token - 1));
	size_t r_paren = buf.find(')');
	size_t third_token = buf.find(' ', r_paren + 1) + 1;
	std::string comm = buf.substr(second_token + 1, third_token - second_token - 3);

	const int s_idx_len = 30;
	std::array<std::string::size_type, s_idx_len> s_idx;
	s_idx[0] = buf.find(' ', third_token);
	std::cout << "third_token/s_idx[0]: " << third_token << "/" << s_idx[0]
			  << "\n";
	for (int i = 1; i < s_idx_len; i++) {
		s_idx[i] = buf.find(' ', s_idx[i - 1] + 1);
	}
	/*
	std::copy(s_idx.begin(), s_idx.end(),
			  std::ostream_iterator<std::string::size_type>(std::cout, " "));
			  */
	pid_t ppid = stoi(buf.substr(s_idx[0], s_idx[1]));
	std::string state = buf.substr(third_token, s_idx[0] - third_token);
	unsigned long utime = stoul(SUBSTR_BY_IDX(11));
	unsigned long stime = stoul(SUBSTR_BY_IDX(12));
	unsigned long vsize = stoul(SUBSTR_BY_IDX(20));
	unsigned long rss = stoul(SUBSTR_BY_IDX(21));
	std::cout << pid << "/" << comm << "/" << state << "/" << ppid << "/"
			  << vsize << "/" << rss << "\t" << utime << "/" << stime << "\n";
	return true;
}

int main() {
	int cnt = 0;
	for (int i = 1000; cnt < 20; i++) {
		std::stringstream filename;
		filename << "/proc/" << i << "/stat";
		// readfile(filename, out, 100);
		if (parse_proc(filename.str()))
			cnt++;
	}
}
