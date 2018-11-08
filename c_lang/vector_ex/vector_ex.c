#include <stdio.h>
#include "common.h"
#include "mvector.h"

extern int update_list(struct item * arr, int size);

int main(int argc, const char *argv[])
{
	struct item a[] = {
		{12, "a"},	{11, "b"},
		{13, "c"},	{5, "d"},
		{6, "e"},	{7, "f"},
	};
    int a_size = sizeof(a)/sizeof(a[0]);
	struct item b[] = {
		{12, "a"},	{1, "x"},
		{13, "c"},	{5, "d"},
		{6, "e"},	{99, "y"},
	};
    int b_size = sizeof(b)/sizeof(b[0]);

	update_list(a, a_size);
	update_list(b, b_size);

    return 0;
}
