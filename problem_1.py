# direct solution
def simple_way(n, a, b):
    sum = 0
    for i in range(n):
        if (i % a == 0 or i % b == 0):
            sum += i
    return sum

# solution by progression
def progression(n, a):
    p = n//a
    return a*(p*(p + 1))//2

n = 1000
a = 3
b = 5

print("simple_way -", simple_way(n, a, b))

print("progression -", progression(n, a) + progression(n, b) - progression(n, a*b))

