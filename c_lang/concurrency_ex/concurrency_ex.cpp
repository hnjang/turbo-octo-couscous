#include <iostream>
#include <thread>
#include <mutex>
#include <iterator>
#include <algorithm>
#include <vector>
#include <unistd.h>

class C {
	std::vector<int> v;
	mutable std::mutex mutex_;

  public:
	C() {}
	void update(const std::vector<int> &new_v) {
		std::lock_guard<std::mutex> lock(mutex_);
		v = new_v;
	}
	bool check(int x) const {
		std::lock_guard<std::mutex> lock(mutex_);
		return std::find(v.begin(), v.end(), x) != v.end();
	}
	/* dump() is not essential */
	void dump() const {
		std::lock_guard<std::mutex> lock(mutex_);
		std::cout << "dump: ";
		std::copy(v.begin(), v.end(),
				  std::ostream_iterator<int>(std::cout, " "));
		std::cout << "\n";
	}
};

// create an instance gloablly
C g_c;

void updater_thread() {
	std::cout << "start updater_thread\n";
	while (true) {
		std::vector<int> v;
		for (int i = 0; i < 10; i++) {
			v.push_back(rand() % 10 + 1);
		}
		std::sort(v.begin(), v.end());
		g_c.update(v);
		std::cout << "updated!!!\n";
		std::copy(v.begin(), v.end(),
				  std::ostream_iterator<int>(std::cout, " "));
		std::cout << "\n";
		sleep(5);
	}
}

void reader_thread() {
	std::vector<int> v{1, 2, 3, 5};
	while (true) {
		std::cout << "check: non-exist item: ";
		for (int e : v) {
			if (!g_c.check(e)) {
				std::cout << e << " ";
			}
		}
		std::cout << "\n";
		sleep(1);
	}
}

int main() {
	std::thread t_up(updater_thread);
	std::thread t_r(reader_thread);
	t_up.join();
	t_r.join();
}

