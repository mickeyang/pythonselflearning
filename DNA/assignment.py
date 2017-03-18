def get_length(dna):
    """ (str) -> int
    Return the length of the DNA sequence dna.
    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    if(len(dna) > 0):
        return len(dna)
    return 0

def is_longer(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.
    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if(len(dna1) > 0 and len(dna2) > 0):
        return(len(dna1) > len(dna2))
    return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int
    Return the number of occurrences of nucleotide in the DNA sequence dna.
    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    if(len(dna) > 0 and len(nucleotide) > 0):
        return dna.count(nucleotide)
    return 0

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.
    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if(len(dna1) > 0 and len(dna2) > 0):
        return(dna1.count(dna2) > 0)
    return False