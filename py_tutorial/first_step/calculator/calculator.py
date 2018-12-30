
def tokenize(string):
    result = []
    op_str = '+-*/()'
    p = 0
    while True:
        if len(string) == 0:
            break
        if len(string) <= p:
            result.append(string)
            break
        if string[p] not in op_str:
            p += 1
        else:
            result.append(string[:p])
            result.append(string[p])
            string = string[p+1:]
            p = 0
    return result

def make_postfix(infix):
    s = 0
    op_str = '+-*/()'
    p = 0

expr = input()
infix = tokenize(expr)
print(infix)

