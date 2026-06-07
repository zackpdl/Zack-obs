# Puran Paodensakul
# 542
# 6611140

class obj:
    def __init__(self,w,v):
        self.w = w
        self.v = v
        self.r = v/w

x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(N):
    item.append(obj(int(w[i]),int(v[i])))

maxV = 0
count = 0
upperBound = sum([item[i].v for i in range(N)])

def dfs(i, sumW, sumV):
    global maxV, count
    count += 1

    if sumW > M: return


    if sumV + Bound(i, M - sumW) <= maxV: return

    if i == N:
        maxV = max(maxV, sumV)
        return

    dfs(i+1, sumW+item[i].w, sumV+item[i].v)
    dfs(i+1, sumW, sumV)

def Bound(i, C):
    global item, N

    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < N and f == 1.0:
        wj = min(C-sw, item[j].w)
        f = float(wj)/item[j].w
        sw += f*item[j].w
        sv += f*item[j].v
        j += 1
    return sv

def getKey(x):
    return x.r

item.sort(key=getKey, reverse=True)

dfs(0,0,0)
print(maxV)
print(f"Number of recursive calls: {count}")
