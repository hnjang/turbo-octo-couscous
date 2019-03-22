#pragma once

#ifdef __cplusplus
#define EXTERNC extern "C"
#else
#define EXTERNC
#endif

EXTERNC int update_list(struct item * arr, int size);

#ifdef USE_MV_MAIN
#pragma message (" you reach here L12. mvector.h ")

EXTERNC int main(int argc, const char *argv[]);
#endif

#undef EXTERNC

