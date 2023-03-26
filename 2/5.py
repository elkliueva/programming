def PatternToNumber(dna):
    if dna == '':
        return 0
    symbol = dna[-1]
    prefix = dna[0:-1]
    return 4 * PatternToNumber(prefix) + symbol_to_number(symbol)
    
def symbol_to_number(symbol):
    if symbol == 'A': 
        return 0 
    elif symbol == 'C': 
        return 1 
    elif symbol == 'G': 
        return 2 
    elif symbol == 'T': 
        return 3
def ComputingFrequencies(genome, k):
    freq_array = [0] * (4**k)
    for i in range(len(genome)-k+1):
        pattern = genome[i:i+k]
        j = PatternToNumber(pattern)
        freq_array[j] += 1
    return freq_array

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

def BetterClumpFinding(text, k, t, L):
    result = [] 
    freqArray = ComputingFrequencies(text[0:L], k) 
    clump= [False]*(4**k) 
    for i in range(4**k): 
        if freqArray[i] >= t: 
            clump[i] = True 
        else: 
            clump[i] = False 
    for i in range(1, len(text) - L + 1): 
        preffNum = PatternToNumber(text[i-1:i+k-1]) 
        suffNum = PatternToNumber(text[i+L-k:i+L]) 
        freqArray[preffNum] -= 1 
        freqArray[suffNum] += 1 
        if freqArray[suffNum] >= t:     
            clump[suffNum] = True 
    for i in range(4**k): 
        if clump[i] == True: 
            result.append(NumberToPattern(i, k)) 
    return result 
    
    

genome = input()
k, L, t = map(int, input().split())
print(*BetterClumpFinding(genome, k, t, L))
