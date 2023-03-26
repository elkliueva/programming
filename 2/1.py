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

dna = input()
print(PatternToNumber(dna))