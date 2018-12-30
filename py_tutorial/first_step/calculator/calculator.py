
def tokenize(string):
    result = []
    op_paren_str = '+-*/()'
    p = 0
    while True:
        if len(string) == 0:
            break
        if len(string) <= p:
            result.append(string)
            break
        if string[p] not in op_paren_str:
            p += 1
        else:
            if p > 0:
                result.append(string[:p])
            result.append(string[p])
            string = string[p+1:]
            p = 0
    return result

def make_postfix(infix):
    op_str = '+-*/'
    op_rank = {
        '+' : 1, '-' : 1,
        '*' : 2, '/' : 2,
		'(' : 3
        }
    stack = []
    postfix = []
    for e in infix:
        if e == '(':
            stack.append(e)
        elif e == ')':
            op = stack.pop()
            while op != '(':
                postfix.append(op)
                op = stack.pop()
        elif e in op_str:
            while len(stack) > 0 and op_rank[e] >= op_rank[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(e)
        else:
            postfix.append(e)

    while len(stack) > 0:
        postfix.append(stack.pop())
    return postfix

expr = input()
infix = tokenize(expr)
print(infix)
postfix = make_postfix(infix)
print(postfix)
