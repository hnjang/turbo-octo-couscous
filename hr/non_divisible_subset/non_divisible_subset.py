#!/usr/bin/python3

class big_number:
    def __init__(self, v=None):
        self.data = ['0'] * 200
        i = 0
        if v==None: return
        while v > 0:
            self.data[i] = str(int(v % 10))
            v = (v - v%10)//10
            i += 1
        #print('init() ', self.data)
        return

    def add(self, x):
        s = self.data
        c = 0
        for i in range(len(s)):
            r = int(s[i]) + int(x.data[i]) + c
            c = r // 10
            s[i] = str(r % 10)
    def mult(self, x):
        if x<=0: return None
        x -= 1
        t = big_number()
        t.data = list(self.data) # copy
        for xx in range(x):
            self.add(t)
    def pr_value(self):
        string = ''
        heading_z = True
        #print(len(self.data))
        for i in range(len(self.data)-1, -1, -1):
            if heading_z and self.data[i]=='0': continue
            heading_z = False
            string = string + str(self.data[i])
        print(string)

def extraLongFactorials(n):
    if n<0: return None
    a = big_number(1)
    if n>1:
        for i in range(2,n+1):
            a.mult(i)
    a.pr_value()

def nonDivisibleSubset(k, S):
    mod_cnt = [0]*k
    for s in S:
        c = s%k
        mod_cnt[c] += 1
    #print(mod_cnt)
    result = 0
    result += min(mod_cnt[0], 1)
    for i in range(1,(k+1)//2):
        result += max(mod_cnt[i], mod_cnt[k-i])
    if k%2==0:
        result += min(mod_cnt[k//2], 1)
    return result

if __name__ == '__main__':
    '''
    a = big_number(100)
    a.pr_value()

    b = big_number(10)
    b.pr_value()

    a.mult(33)
    a.pr_value()
    '''
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    S = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, S)
    print(result)

