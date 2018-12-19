#include <iostream>
#include <string>
#include <sstream>
#include <exception>
using namespace std;

// if we have to inherit 'exception' class.
class BadLengthException : public exception {
	string err_str;

  public:
	BadLengthException(int n) {
		err_str = to_string(n);
	}
	virtual const char *what() const throw() { return err_str.c_str(); }
};

// if we don't have to inherit.
class __BadLengthException {
	int n;

  public:
	__BadLengthException(int n) : n{n} {}
	const int what() const throw() { return n; }
};

bool checkUsername(string username) {
	bool isValid = true;
	int n = username.length();
	if(n < 5) {
		throw BadLengthException(n);
	}
	for(int i = 0; i < n-1; i++) {
		if(username[i] == 'w' && username[i+1] == 'w') {
			isValid = false;
		}
	}
	return isValid;
}

int main() {
	int T; cin >> T;
	while(T--) {
		string username;
		cin >> username;
		try {
			bool isValid = checkUsername(username);
			if(isValid) {
				cout << "Valid" << '\n';
			} else {
				cout << "Invalid" << '\n';
			}
		} catch (BadLengthException e) {
			cout << "Too short: " << e.what() << '\n';
		}
	}
	return 0;
}
