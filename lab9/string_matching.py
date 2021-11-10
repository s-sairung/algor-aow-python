import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input/test.txt')
f = open(filename)
lines = [line.strip() for line in f.readlines()]
f.close()

# it's meeeeeeeeeeeeeeee mp้!

# print(lines)
global alphabets
global m, n
global pattern
global text
alphabets = lines[0].split(' ')
m, n = lines[1].split(' ')
m = int(m)
n = int(n)
p = lines[2].split(' ')
pattern = ''
text = ''
for c in p:
    pattern = pattern + c
print(pattern)
t = lines[3].split(' ')
for c in t:
    text = text + c
print(text)

def kmp_matcher(t: str, p: str):
    pi = compute_prefix_function(p)
    print(pi)
    q = 0
    ans = []
    for i in range(0, n): # 0.....n - 1 p0 a1 t2 t3 e4 r5 n6
        while q > 0 and p[q] != t[i]:
            q = pi[q - 1]
        if p[q] == t[i]:
            q += 1
        if q == m:
            # print("Pattern occurs with shift " + str(i - m + 2))
            ans.append(i - m + 1)
            q = pi[q - 1]
    return ans


def compute_prefix_function(p: str):
    pi = [0 for i in range(m)] # pi[0 .. m - 1] <-- index
    k = 0
    pi[0] = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k - 1]
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi


print("------------------------------KMP--------------------------------------")

a1 = kmp_matcher(text, pattern)
text_reversed = text[::-1]
# pattern_reversed = pattern[::-1]

a2 = kmp_matcher(text_reversed, pattern)
a2.reverse()

print('ans count = ' + str(len(a1) + len(a2)))
for a in a1:
    print(str(a + 1) + ' LR')

for a in a2:
    print(str(n - a) + ' RL')


def naive_string_matcherdedded(t: str, p: str):
    ans = []
    for s in range(n - m + 1):
        if p == t[s: s + m]:
            # print('Pattern occurs with shift ' + str(s))
            ans.append(s)
    return ans


print("------------------------------Naive------------------------------------")
a3 = naive_string_matcherdedded(text, pattern)
a4 = naive_string_matcherdedded(text_reversed, pattern)
a4.reverse()

print('ans count = ' + str(len(a3) + len(a4)))
for a in a3:
    print(str(a + 1) + ' LR')

for a in a4:
    print(str(n - a) + ' RL')

