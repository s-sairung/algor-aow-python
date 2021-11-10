import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/9.1.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

# it's meeeeeeeeeeeeeeee mp้!

print(lines)
global alphabets
global m, n
global pattern
global text
alphabets = lines[0].split(' ')
m, n = lines[1].split(' ')
m = int(m)
n = int(n)
pattern = lines[2]
text = lines[3]

def kmp_matcher(t: str, p: str):
    pi = compute_prefix_function(p)
    q = 0
    for i in range(1, n + 1): # 0.....n-1
        while q > 0 and p[q + 1] != t[i]:
            q = pi[q]
        if p[q + 1] == t[i]:
            q += 1 
        if q == m:
            print("Pattern occurs with shift " + str(i - m))
            q = pi[q]


def compute_prefix_function(p: str):
    pi = [0 for i in range(m)] # pi[0 .. m - 1] <-- index
    k = 0
    
    for q in range(2, m + 1):
        while k > 0 and p[k + 1] != p[q]:
            k = pi[k]
        if p[k + 1] == p[q]:
            k = k + 1
        pi[q] = k
    return pi

kmp_matcher(text, pattern)

