from fractions import Fraction
import math

def compute_moebius_function(n):
    if n == 1:
        return 1
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    if len(factors) == 0:
        return 0
    return -1 if len(factors) % 2 else 1

def compute_continued_fraction_expansion(x, max_terms=50):
    terms = []
    for _ in range(max_terms):
        a = int(x)
        terms.append(a)
        x -= a
        if x == 0:
            break
        x = 1 / x
    return terms

def compute_partial_sum(n, continued_fraction, moebius_function):
    partial_sum = 0
    for i in range(1, n + 1):
        term_of_continued_fraction = continued_fraction[i - 1] if i - 1 < len(continued_fraction) else 0
        moebius_result = moebius_function(term_of_continued_fraction)
        squared_result = moebius_result ** 2
        partial_sum += squared_result * (i + 1)
    return partial_sum

# Hardcoded approximate value of the Feigenbaum constant
feigenbaum_constant_hardcoded = float("4." +
"6692016091029906718532038204662016172581855774757686327456513430" +
"0413433021131473713868974402394801381716598485518981513440862714" +
"2027932522312442988890890859944935463236713411532481714219947455" +
"6443658237932020095610583305754586176522220703854106467494942849" +
"8145339172620056875566595233987560382563722564800409510712838906" +
"1184470277585428541980111344017500242858538249833571552205223608" +
"7250291678860362674527213399057131606875345083433934446103706309" +
"4520191158769724322735898389037949462572512890979489867683346116" +
"2688911656312347446057517953912204556247280709520219819909455858" +
"1946136877445617396074115614074243754435499204869180982648652368" +
"4387027996490173977934251347238087371362116018601281861020563818" +
"1835409759847796417390032893617143215987824078977661439139576403" +
"7760537119096932066998361984288981837003229412030210655743295550" +
"3888458497370347275321219257069584140746618419819610061296401614" +
"8771294441590140546794180019813325337859249336588307045999993837" +
"5411726563553016862529032210862320550634510679399023341675")

# Compute the Continued Fraction Expansion of the Feigenbaum constant
A159766 = compute_continued_fraction_expansion(feigenbaum_constant_hardcoded)

# Calculate the partial sums for the first 20 terms of the sequence
terms_to_compute = 20
partial_sums_sequence = [compute_partial_sum(n, A159766, compute_moebius_function) for n in range(1, terms_to_compute + 1)]

# Known values of the sequence A132315 for validation
A132315_known = [0, 2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, 152, 170, 189, 209, 230]

# Validate the computed sequence against the known values
is_valid = partial_sums_sequence == A132315_known[1:21]
print(f"Validation result: {is_valid}")
