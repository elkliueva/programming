from functools import reduce

def HammingDistance(s1, s2):
    return reduce(lambda x, y: x + (y[0] != y[1]), zip(s1, s2), 0)

def ApproximatePatternMatch(pattern, text, d):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        pattern_prime = text[i:i+len(pattern)]
        if HammingDistance(pattern, pattern_prime) <= int(d):
            positions.append(i)
    return positions
pattern = input()
text = input()
d = int(input())
print(*ApproximatePatternMatch(pattern, text, d))