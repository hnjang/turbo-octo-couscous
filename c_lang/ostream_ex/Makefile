CXX=g++
CXXFLAGS=-std=c++11

CPPFLAGS=-g
LDFLAGS=-g
#LDLIBS=$(shell root-config --libs)
RM=rm -f

CPP_SRCS=ostream_ex.cpp
OBJS=$(subst .cpp,.o,$(CPP_SRCS))
ostream_ex: $(OBJS)
	$(CXX) $(LDFLAGS) -o ostream_ex $(OBJS) $(LDLIBS)

clean:
	$(RM) $(OBJS)
distclean:
	$(RM) ostream_ex

