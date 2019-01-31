CXX=g++
CXXFLAGS=-g -std=c++11 -pthread

CPPFLAGS=-g
LDFLAGS=-g -pthread
#LDLIBS=$(shell root-config --libs)
RM=rm -f

CPP_SRCS=concurrency_ex.cpp
OBJS=$(subst .cpp,.o,$(CPP_SRCS))

ex: $(OBJS)
	$(CXX) -o ex $(LDFLAGS) $(OBJS) $(LDLIBS)

clean:
	$(RM) $(OBJS)
distclean:
	$(RM) ex

