# original source code can be retrieved from
#  https://medium.com/@tarun27sh/python-scripts-for-gdb-9b17ca090ac5

#import sys, os


class PrintStructC99(gdb.Command):
    def __init__(self):
        super(PrintStructC99, self).__init__("print_struct_c99",
                                             gdb.COMMAND_USER)

    def get_count_heading(self, string):
        for i, s in enumerate(string):
            if s != ' ': break
        return i

    def extract_typename(self, string):
        first_line = string.split('\n')[0]
        return first_line.split('=')[1][:-1].strip()

    def invoke(self, arg, from_tty):
        ret_ptype = gdb.execute('ptype {}'.format(arg), to_string=True)
        tname = self.extract_typename(ret_ptype)
        print('{} {} = {{'.format(tname, arg))
        r = gdb.execute('p {}'.format(arg), to_string=True)
        r = r.split('\n')
        for rr in r[1:]:
            if '=' not in rr:
                print(rr)
                continue
            hs = self.get_count_heading(rr)
            rr_s = rr.strip().split('=')
            rr_rval = rr_s[1].strip().split(' ')[0]
            print(' ' * hs + '.' + rr_s[0] + '= ' + rr_rval)


def setup():
    print('Running GDB from: %s\n' % (gdb.PYTHONDIR))
    gdb.execute("set print pretty")


setup()
# instantiate
PrintStructC99()
