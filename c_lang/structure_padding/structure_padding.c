#include <stdint.h>
#include <stdio.h>

// Alignment requirements
// (typical 32 bit machine)

// char         1 byte
// short int    2 bytes
// int          4 bytes
// double       8 bytes

// structure A
typedef struct structa_tag
{
   char c;
   // short int s;
   int16_t s;
} structa_t;

struct a_packed
{
   char c;
   // short int s;
   int16_t s;
} __attribute__((packed));

// structure B
typedef struct structb_tag
{
   // short int s;
   int16_t s;
   char c;
   int i;
} structb_t;

// structure C
typedef struct structc_tag
{
   char c;
   double d;
   int s;
} structc_t;

// structure D
typedef struct structd_tag
{
   double d;
   int s;
   char c;
} structd_t;

int main()
{
   printf("sizeof(int) = %lu\n", sizeof(int));
   printf("sizeof(structa_t) = %lu\n", sizeof(structa_t));
   printf("sizeof(structa_t) = %lu\n", sizeof(struct a_packed));
   printf("sizeof(structb_t) = %lu\n", sizeof(structb_t));
   printf("sizeof(structc_t) = %lu\n", sizeof(structc_t));
   printf("sizeof(structd_t) = %lu\n", sizeof(structd_t));

   return 0;
}
