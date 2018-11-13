#include <stdio.h>
#include "common.h"
#include "mvector.h"

extern int update_list(struct item * arr, int size);

int main(int argc, const char *argv[])
{
	struct item a[] = {
        { 12, "a", 12 },
        { 11, "b", 11 },
        { 13, "c", 13 },
        { 5, "d", 5 },
        { 6, "e", 6 },
        { 7, "f", 7 },
	};
    int a_size = sizeof(a)/sizeof(a[0]);
	struct item b[] = {
		{ 12, "a", 20 },
        { 1, "x", 5 },
        { 13, "c", 5 },
        { 5, "d", 10 },
        { 6, "e", 6 },
        { 99, "y", 5 },
	};
    int b_size = sizeof(b)/sizeof(b[0]);

	update_list(a, a_size);
	update_list(b, b_size);

    return 0;
}
