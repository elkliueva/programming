def func(k, exp):
    n = len(k)
    count = [0]*10
    output = [0]*n
    
    for i in range(n):
        index = k[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = k[i] // exp
        output[count[index % 10] - 1] = k[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        k[i] = output[i]


def digital(k):
    max_elem = max(k)
    exp = 1
    
    while max_elem // exp > 0:
        func(k, exp)
        print(' '.join(map(str, k)))
        exp *= 10


k = list(map(int, input().split()))
digital(k)



