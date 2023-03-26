def NumberToPattern(index, k):
    dna = ''
    for i in range(k):
        remainder = index % 4
        if remainder == 0:
            dna = 'A' + dna
        elif remainder == 1:
            dna = 'C' + dna
        elif remainder == 2:
            dna = 'G' + dna
        else:  # remainder == 3:
            dna = 'T' + dna

        index //= 4

    return dna
index, k = map(int, input().split())
print(NumberToPattern(index, k))