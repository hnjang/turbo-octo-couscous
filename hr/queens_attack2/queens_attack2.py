#!/usr/bin/python3
import sys
from pprint import pprint

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

def countSquareOld(n, r_q, c_q, board, s):
    print('countSquareOld: entry')
    result = 0
    cur = [r_q-1, c_q-1]
    while True:
        cur = [cur[x]+s[x] for x in range(2)]
        if cur[0] < 0 or (cur[1]<0): return result
        if cur[0] >= n or (cur[1]>=n): return result
        #print('L68',cur)
        if board[cur[0]][cur[1]]:
            #print('L6x. this will not be counted. there is a obstacle. ',cur)
            return result
        #print('L6x. this is counted',cur)
        result += 1

def countSquare(n, line, qc):
    step = [1,-1]
    result = 0
    for s in step:
        cur = qc
        print('qc/s : %d/%d'%(qc,s))
        while True:
            cur = cur + s
            if cur < 0 or cur >= n: break
            if line[cur]:
                print('L8x. this will not be counted. there is a obstacle. ',cur)
                break
            print('L8x. this is counted',cur)
            result += 1
    return result

def countSquareDiag(n, line, q, step):
    result = 0
    for s in step:
        cur = q
        print('q/s : ',(q,s))
        while True:
            cur = [cur[x]+s[x] for x in range(2)]
            if cur[0] < 0 or (cur[1]<0): break
            if cur[0] >= n or (cur[1]>=n): break
            if line[cur[1]]:
                #print('L8x. this will not be counted. there is a obstacle. ',cur)
                break
            #print('L8x. this is counted',cur)
            result += 1
    return result

def queensAttack(n,k,r_q,c_q, obstacles):
    print('queensAttack: entry')
    #board = [[False] * n for __ in range(n)]
    rc_lines = [[False]*n for __ in range(2)]
    diag_lines = [[False]*n for __ in range(2)]
    q = [r_q-1, r_q-1]
    q_diag = [sum(q), q[0]-q[1]+n-1]
    for o in obstacles:
        for i in range(2):
            if (o[i]-1)==q[i]:
                rc_lines[i][q[(i+1)%2]-1] = True
        o_diag = [sum(o)-2, o[0]-o[1]+n-1]
        for i in range(2):
            if (o_diag[i]==q_diag[i]):
                diag_lines[i][q[1]] = True
    count = 0
    pprint(rc_lines)
    pprint(diag_lines)
    for i in range(2):
        print('count for rc lines (%d)'%i)
        count += countSquare(n, rc_lines[i], q[(i+1)%2])
    print('count for diag lines')
    step = [
            [[1,-1],[-1,1]],
            [[1,1],[-1,-1]]
            ]
    for i in range(2):
        count += countSquareDiag(n, diag_lines[i], q, step[i])
    return count

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
