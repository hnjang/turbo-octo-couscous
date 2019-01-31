CXX=g++
CXXFLAGS=-g -std=c++11 -pthread

CPPFLAGS=-g
LDFLAGS=-g
#LDLIBS=$(shell root-config --libs)
RM=rm -f

CPP_SRCS=concurrency_ex.cpp
OBJS=$(subst .cpp,.o,$(CPP_SRCS))

#ex: $(OBJS)
#	$(CXX) $(CXXFLAGS) $(OBJS) $(LDLIBS)

target: $(OBJS)
	$(CXX) $(CXXFLAGS) -o ex concurrency_ex.cpp

clean:
	$(RM) $(OBJS)
distclean:
	$(RM) ex

