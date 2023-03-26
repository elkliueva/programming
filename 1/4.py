def f(dna):
    res = ''
    for i in dna[::-1]:
        res += 'A' if i == 'T' else \
                    'C' if i == 'G' else \
                    'G' if i == 'C' else 'T'
    return res

print(f('AAAACCCGGT'))