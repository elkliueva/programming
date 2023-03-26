def FasterFrequentWords(text, k):
    frequent_patterns = set()
    frequency_array = ComputingFrequencies(text, k)
    max_count = max(frequency_array)

    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = NumberToPattern(i, k)
            frequent_patterns.add(pattern)

    return sorted(frequent_patterns)

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
    
text = input()
k = int(input())

print(*FasterFrequentWords(text, k))