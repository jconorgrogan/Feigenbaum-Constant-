from sympy import mobius

# Continued Fraction for first Feigenbaum Constant,  A159766 - see https://oeis.org/A159766
feigenbaum_sequence_full = [
    4, 1, 2, 43, 2, 163, 2, 3, 1, 1, 2, 5, 1, 2, 3, 80, 2, 5, 2, 1, 1, 1, 33, 1, 1, 53, 1, 1, 1, 1, 1, 1, 6, 1, 1, 2, 2, 1, 1, 239, 1, 3, 31, 1, 1, 11, 1, 13, 123, 2,
    2, 2, 2, 13, 15, 1, 2, 3, 3, 1, 3, 1, 1, 6, 1, 3, 1, 1, 13, 8, 1, 7, 1, 2, 1, 8, 7, 1, 17
]

# Updated sequence for A008683 (Möbius function) https://oeis.org/A008683
mobius_sequence_full = [
    1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0, -1, 0, -1, 0, 1, 1, -1, 0, 0, 1, 0, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1, 1, 1, 0, -1, -1, -1, 0, 0, 1, -1, 0, 0, 0,
    1, 0, 1, 1, -1, 0, -1, 1, 0, 0, 1, -1, -1, 0, 1, -1, -1, 0, -1, 1, 0, 0, 1, -1
]

# Function to calculate a(n)
def corrected_calculate_a_n(n, feigenbaum_seq, mobius_seq):
    sum_seq = 0
    for i in range(n + 1):
        # Adjusting for zero-based indexing
        feigenbaum_element = feigenbaum_seq[i] if i < len(feigenbaum_seq) else 0
        mobius_value = mobius(feigenbaum_element)
        sum_seq += mobius_value**2 * (i + 1)
    return sum_seq

# Calculate the first 79 terms of A132315 with the full sequences
corrected_a132315_full = [corrected_calculate_a_n(i, feigenbaum_sequence_full, mobius_sequence_full) for i in range(79)]
corrected_a132315_full
