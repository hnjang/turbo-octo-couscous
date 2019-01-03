#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
	void *handle;
	double (*cosine)(double);
	int (*h)();
	int (*get_sum)();
	char *error;

	handle = dlopen("../lib_ex/lib_ex.so", RTLD_LAZY);
	if (!handle) {
		fprintf(stderr, "%s:%d: %s\n", __func__, __LINE__, dlerror());
		exit(EXIT_FAILURE);
	}

	dlerror(); /* Clear any existing error */

	/* Writing: cosine = (double (*)(double)) dlsym(handle, "cos");
		would seem more natural, but the C99 standard leaves
		casting from "void *" to a function pointer undefined.
		The assignment used below is the POSIX.1-2003 (Technical
		Corrigendum 1) workaround; see the Rationale for the
		POSIX specification of dlsym(). */

	*(void **)(&h) = dlsym(handle, "hello");
	*(void **)(&get_sum) = dlsym(handle, "get_sum");

	if ((error = dlerror()) != NULL) {
		fprintf(stderr, "%s\n", error);
		exit(EXIT_FAILURE);
	}

	(*h)();
	printf("get_sum: %d\n", (*get_sum)(1, 2));
	dlclose(handle);
	exit(EXIT_SUCCESS);
}
