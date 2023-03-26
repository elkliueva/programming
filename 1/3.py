t = input()
k = int(input())
def f(t, k):
    if k > len(t): 
        return None
    if k == len(t): 
        return {t:1}
    list_substr = list()  
    for j in range(len(t) - k + 1):
        list_substr.append( t[j:j+k])
    res = dict()
    for j in range(len(list_substr)):
        key_val = list_substr[j]
        res[key_val] = res.get(key_val, 0) + 1

    return res
res = f(t, k)
max_value = max(res.values())
for key in sorted(res):
    if res[key] == max_value:
        print(key, end=' ')
