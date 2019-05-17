#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>
#include <sys/mman.h>
#include <unistd.h>

using std::cout;
using std::cin;

std::vector<char *> buffs;

std::string catch_line(std::string fname, std::string substr) {
	std::string ret;
	std::ifstream fin;
	fin.open(fname.c_str());
	if (!fin.is_open()) {
		cout << "file open failed.\n";
		exit(-1);
	}
	while(!fin.eof()) {
		std::string s;
		std::getline(fin, s);
		std::transform(s.begin(), s.end(), s.begin(), ::tolower);
		if (s.find(substr) != std::string::npos) {
			ret += s + "\n";
		}
	}
	fin.close();
	return ret;
}

int alloc_lock() {
	cout << "enter memory size in MB: ";
	int size;
	cin >> size;
	if (size==-1)
		return 1;
	cout << "let's call malloc. size=" << size << "\n";
	const size_t sz_1m = 1024 * 1024;
	char * buf = (char *)malloc(sz_1m*size);
	if (!buf) {
		cout << "malloc failed.\n";
	}
	int ret = mlock(buf, sz_1m*size);
	if (ret) {
		cout << "mlock failed. ret=" << ret << "\n";
	}
	buffs.push_back(buf);
#if 0
	std::ifstream fin;
	fin.open("/proc/meminfo");
	if (!fin.is_open()) {
		cout << "file open failed.\n";
		exit(-1);
	}
	while(!fin.eof()) {
		std::string s;
		std::getline(fin, s);
		std::string mem_avail("MemAvailable");
		if (s.find(mem_avail) != std::string::npos) {
			cout << s << "\n";
		}
	}
	fin.close();
#endif
	cout << catch_line(std::string("/proc/meminfo"), std::string("memavailable"));

	pid_t pid = getpid();
	cout << "pid: " << pid << "\n";
	std::string fname = std::string("/proc/") + std::to_string(pid) + std::string("/status");
	cout << catch_line(fname, std::string("rss"));


	return 0;
}

int main() {
	while(true) {
		if (alloc_lock()) {
			cout << "quiting...\n";
			break;
		}
	}
}
