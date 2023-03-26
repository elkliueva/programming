p = input()
t = input()
def f(a, b):
    result = []
    for i in range(len(b) - len(a) + 1):
        if b[i:i+len(a)] == a:
            result.append(i)
    return result

print(' '.join(str(x) for x in f(p,t)))