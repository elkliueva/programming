def CountNucleotides(dna):
    nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for n in dna:
        if n in nucleotides:
            nucleotides[n] += 1
    return nucleotides

d =  CountNucleotides("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
for value in d.values():
    print(value, end=' ')