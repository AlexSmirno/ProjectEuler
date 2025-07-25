import math 

def next_k(k):
    if(k > 0):
        return -k
    elif(k < 0):
       return -k + 1
    else:
        return k + 1
    
def gk(k):
    return int(k*(3*k - 1)/2)


def p(n, p_s):
    p = 0
    k = 1
    g_k = gk(k)
    l = len(p_s)
    while(l >= g_k):
        power = int(math.pow((-1), (k - 1)))
        p += power*p_s[n - g_k]
        k = next_k(k)
        g_k = gk(k)
    return p

p_history = [1, 1, 2, 3, 5]

for i in range(100000):
    n = len(p_history)
    new_p = int(p(n, p_history))
    p_history.append(new_p)
    if(new_p % 1_000_000 == 0):
        print(f"p({n}) = {new_p}")
        break;

