CXX=g++
CXXFLAGS=-std=c++11

CPPFLAGS=-g
LDFLAGS=-g
#LDLIBS=$(shell root-config --libs)
RM=rm -f

CPP_SRCS=sc_ex.cpp
OBJS=$(subst .cpp,.o,$(CPP_SRCS))
ostream_ex: $(OBJS)
	$(CXX) $(LDFLAGS) -o sc_ex $(OBJS) $(LDLIBS)

clean:
	$(RM) $(OBJS)
distclean:
	$(RM) sc_ex

