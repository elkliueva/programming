def ComputingFrequencies(genome, k):
    freq_array = [0] * (4**k)
    for i in range(len(genome)-k+1):
        pattern = genome[i:i+k]
        j = PatternToNumber(pattern)
        freq_array[j] += 1
    return freq_array

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

print(*ComputingFrequencies(text, k))