#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ApplicationState {
	int x;
    struct {
        bool use_crash_handler;
        bool use_abort_handler;
    } signal;

    struct {
        unsigned char python;
    } exit_code_on_error;
};

int main() {
	struct ApplicationState as;
	as.signal.use_crash_handler = true;
	as.signal.use_abort_handler = false;
	as.exit_code_on_error.python = 'X';
	abort();
}
