#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#I have already programmed a LCM generator.  Unfortunately, it cannot handle 1-20.  So I used python as a calculator below.

answer = 1 #initialization

primes = [2, 3, 5, 7, 11, 13, 17, 19] #these are critical

neglected_nums = [1, 6, 10, 12, 14, 15, 18, 20] #multiples of primes to their first power

numbers_of_interest = [4, 8, 9, 16] #powers of primes

consequent_repeats = [2, 2, 3, 2] #further necessary primes

necessary_multiples = primes + consequent_repeats

for k in necessary_multiples:
    answer = k * answer

print(answer)