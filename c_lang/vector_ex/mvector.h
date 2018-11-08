#pragma once

#ifdef __cplusplus
#define EXTERNC extern "C"
#else
#define EXTERNC
#endif

EXTERNC int update_list(struct item * arr, int size);

#undef EXTERNC

