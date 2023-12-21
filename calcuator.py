import csv
import sys
from fractions import Fraction
from sympy import mobius
import math

# Function to calculate the continued fraction sequence
def continued_fraction_sequence(number, max_length=80):
    quotients = []
    number = Fraction(str(number))  # Convert number to Fraction using string representation

    for _ in range(max_length):
        quotient, remainder = divmod(number, 1)
        quotients.append(int(quotient))

        if remainder == 0:
            break

        number = 1 / remainder

    return quotients

# Function to write data to a CSV file
def write_to_csv(data, filename='continued_fraction_sequence.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for num in data:
            writer.writerow([num])

# Function to calculate a(n) using the Möbius function and user input sequence
def corrected_calculate_a_n(n, user_input_seq):
    sum_seq = 0
    for i in range(n + 1):
        user_input_element = user_input_seq[i] if i < len(user_input_seq) else 0
        mobius_value = mobius(user_input_element)
        sum_seq += mobius_value**2 * (i + 1)
    return sum_seq

# Translated function from PARI/GP to Python for calculating sum of non-fourth powers
def g4(n):
    output = []
    for x in range(1, n + 1):
        r = math.floor(x**(1/4))
        sum4 = r**5/5 + r**4/2 + r**3/3 - r/30
        sn = x*(x+1)/2
        output.append(int(sn - sum4))
    return output

# Increase the limit for integer string conversion
sys.set_int_max_str_digits(100000)  # Adjust this number as needed

# Test the function with a user-input number
user_input_number = "4.6692016091029906718532038204662016172581855774757686327456513430\
0413433021131473713868974402394801381716598485518981513440862714\
2027932522312442988890890859944935463236713411532481714219947455\
6443658237932020095610583305754586176522220703854106467494942849\
8145339172620056875566595233987560382563722564800409510712838906\
1184470277585428541980111344017500242858538249833571552205223608\
7250291678860362674527213399057131606875345083433934446103706309\
4520191158769724322735898389037949462572512890979489867683346116\
2688911656312347446057517953912204556247280709520219819909455858\
1946136877445617396074115614074243754435499204869180982648652368\
4387027996490173977934251347238087371362116018601281861020563818\
1835409759847796417390032893617143215987824078977661439139576403\
7760537119096932066998361984288981837003229412030210655743295550\
3888458497370347275321219257069584140746618419819610061296401614\
8771294441590140546794180019813325337859249336588307045999993837\
5411726563553016862529032210862320550634510679399023341675"
user_input_sequence = continued_fraction_sequence(user_input_number)

# Calculate the sequences
corrected_a132315_full = [corrected_calculate_a_n(i, user_input_sequence) for i in range(70)]
sum_non_fourth_powers_sequence = g4(70)

# Comparing the two sequences
min_length = min(len(corrected_a132315_full), len(sum_non_fourth_powers_sequence))
for i in range(min_length):
    if corrected_a132315_full[i] != sum_non_fourth_powers_sequence[i]:
        print(f"Mismatch at index {i}: Corrected_a132315_full = {corrected_a132315_full[i]}, Sum_non_fourth_powers = {sum_non_fourth_powers_sequence[i]}")
        break
else:
    print("They all match")

