def Neighbours(Pattern, d):
    nuc_dict = {0:'A', 1:'C', 2:'G', 3:'T'}
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffix_neighbors = Neighbours(Pattern[1:], d)
    for neighbor in suffix_neighbors:
        if HammingDistance(Pattern[1:], neighbor) < d:
            for j in range(4):
                neighborhood.append(nuc_dict[j] + neighbor)
        else:
            neighborhood.append(Pattern[0] + neighbor)
    return neighborhood

def HammingDistance(p, q):
    return sum([1 for i, j in zip(p, q) if i != j])

pattern = input().strip()
d = int(input().strip())
print('\n'.join(sorted(Neighbours(pattern, d))))


