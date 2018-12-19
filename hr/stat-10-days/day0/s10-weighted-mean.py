#!/usr/bin/python3
import sys
from pprint import pprint
import collections
from functools import cmp_to_key

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
    C,c = len(G[0]),len(P[0])
    for i in range(last_row+1):
        idx_arr = []
        cur = 0
        while True:
            idx = G[i][cur:].find(P[0])
            if idx==-1: break
            cur = cur+idx
            idx_arr.append(cur)
            #print('L247. i=%d, cur=%d, %s'%(i, cur, G[i]))
            cur += 1
        if (len(idx_arr)<=0): continue
        for idx in idx_arr:
            #print('L25x. i=%d, idx=%d, %s'%(i, idx, G[i]))
            #pprint(G[i][idx:])
            #print('L25x. idx=%d, c=%d C-1:%d'%(idx, c, C-1))
            if idx+c-1 > C-1: continue
            failed = False
            for j in range(1,len(P)):
                if G[i+j][idx:idx+c] != P[j]:
                    failed = True
                    break
            if failed: continue
            return 'YES'
        # end of for-loop.
    return 'NO'

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def gcd_array(arr):
    if len(arr)<1: return None
    elif len(arr)<2: return arr[0]
    g = gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        g = gcd(g, arr[i])
    return g

def getTotalX(a,b):
    count = 0
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i // gcd(lcm, i)
    gcd_b = gcd_array(b)
    mult = min(b) // lcm
    for i in range(1,mult+1):
        if gcd_b%(lcm * i) == 0:
            count += 1
    return count

def migratoryBirds(arr):
    c = collections.Counter(arr)
    # get a sorted list of (k, v)
    m = c.most_common()
    #print(m)
    max_cnt = m[0][1]
    k_list = [m[0][0]]
    for mm in m[1:]:
        if mm[1] != max_cnt: break
        k_list.append(mm[0])
    #print(k_list, min(k_list))
    return min(k_list)

def is_leap_year(year):
    leap = False
    if year >= 1919:
        if (year%4 == 0):
            if (year%100 == 0):
                if (year%400 == 0):
                    leap = True
            else:
                leap = True
    elif year <= 1917:
        if year%4==0:
            leap = True
    return leap

def dayOfProgrammer(year):
    last_day_aug = 31 +28 +31 +30 +31 +30 +31 +31
    if year==1918:
        last_day_aug_1918 = 31 + 15 + 31 +30 +31 +30 +31 +31
        d = 256 - last_day_aug_1918
    else:
        if is_leap_year(year):
            last_day_aug += 1
        d = 256 - last_day_aug
    return '%02d.09.%d'%(d, year)

def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    UD = H*W*2
    RL = 0
    for i in range(H):
        RL += A[i][0]
        for j in range(1,W):
            RL += abs(A[i][j]-A[i][j-1])
        RL += A[i][-1]
    FB = 0
    for i in range(W):
        FB += A[0][i]
        for j in range(1,H):
            FB += abs(A[j][i]-A[j-1][i])
        FB += A[-1][i]
    return UD +RL +FB

def getMoneySpent(keyboards, drives, b):
    m_max = 0
    m_min = 987654321
    for k in keyboards:
        for d in drives:
            c = k + d
            m_min = min(m_min, c)
            if c <= b:
                m_max = max(m_max, c)
    if b < m_min: return -1
    else: return m_max

def absolutePermutation(n, k):
    if k==0: return range(1,n+1)
    if n%(2*k)!=0: return [-1]
    result = []
    plus = True
    for i in range(n):
        result.append(i+k+1 if plus else i-k+1)
        if (i+1)%k==0: plus = not plus
    return result

def getGridFromG2(g2):
    # (1,2,3) => O, 0 => .
    result = []
    for g in g2:
        result.append(g.replace('1','O').replace('2','O').replace('3','O').replace('0','.'))
    return result

def getG2FromGrid(grid):
    # . => 0, O => 3
    result = []
    for g in grid:
        result.append(g.replace('O','3').replace('.','0'))
    return result

def fillBomb(g2):
    result = []
    for g in g2:
        result.append(g.replace('0','3'))
    return result

def getNextG2(g2):
    # 1 => detonate(0), 2 => 1, 3 => 2
    result = []
    r = len(g2)
    c = len(g2[0])
    res = [['0']*(c+2)]
    for g in g2:
        l = list(g)
        l.insert(0,'0')
        l.extend('0')
        res.append(l)
    res.append(['0']*(c+2))
    # detonation
    for i in range(1,r+1):
        for j in range(1,c+1):
            if res[i][j]=='1':
                for d in [[-1,0],[1,0],[0,1],[0,-1]]:
                    res[i+d[0]][j+d[1]] = '1' if res[i+d[0]][j+d[1]]=='1' else '0'
    for i in range(1,r+1):
        for j in range(1,c+1):
            # for now, destroy only itself.
            if res[i][j]=='1': res[i][j]='0'
            if res[i][j]=='2': res[i][j]='1'
            if res[i][j]=='3': res[i][j]='2'
    for i in range(1, r+1):
        result.append(''.join(res[i][1:-1]))
    return result

def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    if n%2==0: return ['O'*c]*r
    if n==1: return grid
    grid2 = getG2FromGrid(grid)
    #print('L417. the result'), pprint(grid2)
    for i in range(2):
        grid2 = getNextG2(grid2)
    grid2 = fillBomb(grid2)
    #print('L421. the result'), pprint(grid2)
    grid2 = getNextG2(grid2) # n = 3
    g_n3 = list(grid2) # copy it
    #print('L424. the result'), pprint(g_n3)
    grid2 = getNextG2(grid2) # n = 4
    grid2 = fillBomb(grid2)
    g_n5 = getNextG2(grid2) # n = 5
    #print('L429. the result'), pprint(g_n5)
    if n%4==3: return getGridFromG2(g_n3)
    elif n%4==1: return getGridFromG2(g_n5)

def permutationEquation(p):
    n = len(p)
    result = []
    for i in range(n):
        result.append(p.index(p.index(i+1)+1)+1)
        #result.append(inv_p(inv_p(i)))
    return result

def appendAndDelete(s, t, k):
    limit = min(len(s),len(t),100)
    #print('limit: ',limit)
    common = 0
    cur = 0
    while cur<limit:
        if s[cur]==t[cur]:
            cur += 1
            common = cur
        else: break
    sub_s = s[common:]
    sub_t = t[common:]
    result_a = len(sub_s)+len(sub_t)
    #print('common idx: ', common)
    #print(sub_s,' / ', sub_t)
    #print('result_a: ',result_a)
    result_b = len(s)+len(t)

    if result_a==k: return 'Yes'
    if result_b<=k: return 'Yes'
    if result_a<k and (k-result_a)%2==0: return 'Yes'
    return 'No'

def matrix2list(matrix):
    final_result = []
    row = len(matrix)
    col = len(matrix[0])
    step = [[0,1],[1,0],[0,-1],[-1,0]]
    tf_mat = [[True]*(2+col)] * 2
    mid_line = [True] +[False] *col +[True]
    for i in range(row):
        tf_mat.insert(1, list(mid_line))
    level = 0
    max_level = min(row,col)//2
    while level < max_level:
        c_row, c_col = level+1, level+1
        c_dir = 0
        tf_mat[c_row][c_col] = True
        result = [matrix[c_row-1][c_col-1]]
        while True:
            r,c = c_row+step[c_dir][0], c_col +step[c_dir][1]
            if tf_mat[r][c]:
                c_dir += 1
                if c_dir==4:  break
                continue
            c_row, c_col = r, c
            tf_mat[r][c] = True
            #print(r,c,matrix[r-1][c-1])
            result.append(matrix[r-1][c-1])
        #print('out of while')
        final_result.append(result)
        level += 1
    return final_result

def list2matrix(mlist):
    row = len(matrix)
    col = len(matrix[0])
    step = [[0,1],[1,0],[0,-1],[-1,0]]
    tf_mat = [[True]*(2+col)] * 2
    mid_line = [True] +[False] *col +[True]
    for i in range(row):
        tf_mat.insert(1, list(mid_line))
    result = [[None]*col for __ in range(row)]
    level = 0
    max_level = min(row,col)//2
    while level < max_level:
        c_row, c_col = level+1, level+1
        c_dir = 0
        pos = 0
        tf_mat[c_row][c_col] = True
        result[c_row-1][c_col-1] = mlist[level][pos]
        while True:
            r,c = c_row+step[c_dir][0], c_col +step[c_dir][1]
            if tf_mat[r][c]:
                c_dir += 1
                if c_dir==4:  break
                continue
            pos += 1
            c_row, c_col = r, c
            tf_mat[r][c] = True
            result[c_row-1][c_col-1] = mlist[level][pos]
        level += 1
    return result

def matrixRotation(matrix, r):
    layer = []
    t = []
    conv_list = matrix2list(matrix)
    rot_list = []
    for l in conv_list:
        pos = r%len(l)
        rot_list.append( l[pos:] + l[:pos] )
    res_mat = list2matrix(rot_list)
    for r in res_mat:
        print( ' '.join([str(x) for x in r]) )
    #pprint(res_mat)

class cs4Item:
    def __init__(self, num, string, idx):
        self.num = num
        self.string = string
        self.idx = idx
    def comparator(a,b):
        num_diff = a.num - b.num
        if num_diff!=0: return num_diff
        else:
            return a.idx - b.idx

def qsort_stable(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        pivot = arr[mid]
        #print('pivot is ')
        #pprint(pivot)
        smaller, greater = [], []
        for a in arr:
            if a[0] < pivot[0]:
                smaller.append(a)
            elif a[0] > pivot[0]:
                greater.append(a)
            else:
                if a[-1] < pivot[-1]:
                    smaller.append(a)
                elif a[-1] > pivot[-1]:
                    # a[-1] must greater than pivot[-1]
                    # because a[-1] is the index. (index is unique value)
                    greater.append(a)
        #print('now start sorting...(%d %d)'%(len(smaller),len(greater)))
        res = qsort_stable(smaller)
        res.extend([pivot])
        res.extend(qsort_stable(greater))
        #print('>>>')
        #pprint(res)
        return res

def countSort(arr):
    mid = len(arr)//2
    '''
    arr2 = []
    for i,a in enumerate(arr):
        arr2.append(cs4Item(int(a[0]), a[1], i))
    '''
    sorted_arr = sorted(arr, key=cmp_to_key(cs4Item.comparator))
    #sorted_arr = qsort_stable(arr2)

    string = ''
    for a in sorted_arr:
        if a.idx < mid:
            string = string +'- '
        else:
            string = string +a.string +' '
    print(string)

if __name__ == '__main__':
    n = int(input())
    v = [int(__) for __ in input().split()]
    w = [int(__) for __ in input().split()]
    acc = 0
    for i in range(n):
        acc += w[i]*v[i]
    print('%.1f' % (acc/sum(w)))
