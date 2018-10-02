#!/usr/bin/python3
import sys
from pprint import pprint
import collections

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
        while True:
            #print('qc/s/cur : %d/%d/%d'%(qc,s,cur))
            cur = cur + s
            if cur < 0 or cur >= n: break
            if line[cur]:
                #print('L8x. this will not be counted. there is a obstacle. ',cur)
                break
            #print('L8x. this is counted',cur)
            result += 1
    return result

def countSquareDiag(n, line, q, step):
    result = 0
    for s in step:
        cur = q
        #print('q/s : ',(q,s))
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
    #print('queensAttack: entry')
    rc_lines = [[False]*n for __ in range(2)]
    diag_lines = [[False]*n for __ in range(2)]
    q = [r_q-1, c_q-1]
    q_diag = [sum(q), q[0]-q[1]+n-1]
    for o in obstacles:
        #print('L118. o:', o)
        for i in range(2):
            if (o[i]-1)==q[i]:
                j = (i+1)%2
                rc_lines[i][o[j]-1] = True
                #print('rc_lines[%d]: mark it as True.'%i,(o, i, o[j]-1))
        o_diag = [sum(o)-2, o[0]-o[1]+n-1]
        for i in range(2):
            if (o_diag[i]==q_diag[i]):
                diag_lines[i][o[1]-1] = True
    count = 0
    #pprint(rc_lines)
    #pprint(diag_lines)
    for i in range(2):
        #print('count for rc lines (%d)'%i)
        count += countSquare(n, rc_lines[i], q[(i+1)%2])
    #print('count for diag lines')
    step = [
            [[1,-1],[-1,1]],
            [[1,1],[-1,-1]]
            ]
    for i in range(2):
        count += countSquareDiag(n, diag_lines[i], q, step[i])
    return count

def organizingContainers(box_cap, ball_cnt):
    counters = [collections.Counter(_) for _ in [box_cap, ball_cnt]]
    for k in counters[0].keys():
        if counters[0][k] != counters[1][k]:
            return 'Impossible'
    return 'Possible'

def encryption(s):
    # remove spaces
    s = s.replace(' ','')

    l = len(s)
    root_l = l**0.5
    r = int(root_l)
    c = r if r*r==l else r+1
    if (r*c < l): r += 1
    #print('l/r/c ',(l,r,c))
    grid = [[' ']*c for __ in range(r)]
    cur = 0
    is_over = False
    for i in range(r):
        for j in range(c):
            if cur>=l:
                is_over = True
                break
            grid[i][j] = s[cur]
            cur += 1
        if is_over: break
    #pprint(grid)

    result = ''
    for j in range(c):
        for i in range(r):
            result += grid[i][j]
        if result[-1]!=' ':
            result += ' '
    return result

def biggerIsGreater(w):
    if len(w)<=1: return 'no answer'
    w = list(w)
    # find the longest non-increasing suffix
    i = len(w) - 1
    while (i>0 and (w[i-1] >= w[i])):
        i -= 1

    if i<=0:
        # it is last permutation
        return 'no answer'

    # now, i is the head index, i-1 is the pivot
    # let's find rightmost element that is greater than the pivot
    j = len(w) - 1
    while (w[j] <= w[i-1]):
        j -= 1

    # swap the pivot with j
    w[j], w[i-1] = w[i-1], w[j]

    # reverse the suffix
    j = len(w) - 1
    while (i<j):
        w[j], w[i] = w[i], w[j]
        j, i = j-1, i+1

    return ''.join(w)

def num2str(num):
    strings = [
'zero',
'one', 'two', 'three', 'four', 'five',
'six', 'seven', 'eight', 'nine', 'ten',
'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five',
'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'thirty'
    ]
    return strings[num]

def minute2str(m):
    if (m==15): return 'quarter'
    if (m==30): return 'half'
    return num2str(m) + (' minute' if m==1 else ' minutes')

def timeInWords(h,m):
    if m==0:
        return num2str(h) + ' o\' clock'
    elif m<=30:
        return minute2str(m) + ' past ' + num2str(h)
    else:
        remaining_m = 60 - m
        hour = h + 1
        if hour==13: hour=1
        return minute2str(remaining_m) + ' to ' + num2str(hour)

def gridSearch(G, P, R, r):
    last_row = R - r # this is 0-based
    for i in range(last_row+1):
        idx = G[i].find(P[0])
        if idx==-1: continue
        for j in range(1,len(P)):
            if G[i+j]

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P, R, r)
        print(result)

