def func(k):
    n = len(k)
    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if k[j] > k[j+1]:
                k[j], k[j+1] = k[j+1], k[j]
                flag = True   
        if not flag:  
            break
        print(' '.join(map(str, k)))
    print(' '.join(map(str, k)))  
    return k

seq = input().split()
seq = list(map(int, seq))
func(seq)