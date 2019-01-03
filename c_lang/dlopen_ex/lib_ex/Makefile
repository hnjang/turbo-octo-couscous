CC 		= $(CROSS_COMPILE)gcc
CXX		= $(CROSS_COMPILE)g++

CFLAGS = -g -c -fPIC
CXXFLAGS = -g -std=c++11
LDFLAGS = -shared

TARGET = lib_ex.so

.SUFFIXES = .c .o

SRCS = lib_ex.c
#CPP_SRCS =

%.o : %.c
	@echo "Compiling C sources $< ..."
	$(CC) -c $(CFLAGS) $< -o $@

%.o : %.cpp
	 @echo "Compiling C++ sources $< ..."
	 $(CXX) -c $(CXXFLAGS) $< -o $@

OBJS = $(SRCS:.c=.o) $(CPP_SRCS:.cpp=.o)

################################################################################
#
# DEFINES COMMAND LINE COMPILE OPTIONS
#

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) -o $@ $(OBJS) $(LDFLAGS)

clean :
	@echo "!!! Delete all object and output files *.o *.a ......"
	rm -vf $(OBJS)
	rm -vf $(TARGET)

rebuild: clean all

