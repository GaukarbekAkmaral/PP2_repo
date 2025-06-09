#1
def grams_to_ounces(grams):
    return 28.3495231 * grams

# Example usage:
print(grams_to_ounces(100))  # Output: 2834.95231



#2
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# Example usage:
f = float(input("Enter temperature in Fahrenheit: "))
print("Celsius:", fahrenheit_to_celsius(f))



#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return "No solution"

# Example usage:
print(solve(35, 94))  # Output: (23, 12)



#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

# Example usage:
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Primes:", filter_prime(nums))



#5
from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for p in perms:
        print(''.join(p))

# Example usage:
s = input("Enter a string: ")
print_permutations(s)



#6
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage:
s = input("Enter a sentence: ")
print(reverse_sentence(s))  # "ready are We"




#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Example usage:
print(has_33([1, 3, 3]))      # → True
print(has_33([1, 3, 1, 3]))   # → False
print(has_33([3, 1, 3]))      # → False




#8
def spy_game(nums):
    code = [0, 0, 7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# Example usage:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # → True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # → True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # → False




#9
import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Example usage:
print(sphere_volume(3))  # ≈ 113.097



#10
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Example usage:
print(unique_list([1, 2, 2, 3, 4, 3, 5]))  # → [1, 2, 3, 4, 5]




#11
def is_palindrome(s):
    s_clean = ''.join(c.lower() for c in s if c.isalnum())  # Remove non-alphanumerics
    return s_clean == s_clean[::-1]

# Example usage:
print(is_palindrome("madam"))         # → True
print(is_palindrome("nurses run"))    # → True
print(is_palindrome("Hello"))         # → False



#12
def histogram(lst):
    for num in lst:
        print('*' * num)

# Example usage:
histogram([4, 9, 7])
# Output:
# ****
# *********
# *******



#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        try:
            guess = int(input())
            guesses_taken += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")






#14
from math import pi
from itertools import permutations

# Import selected functions from above (you can also place them in another file like helpers.py)

def histogram(lst):
    for num in lst:
        print('*' * num)

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def sphere_volume(radius):
    return (4/3) * pi * radius**3

def is_palindrome(s):
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == s_clean[::-1]

def print_permutations(s):
    perms = permutations(s)
    for p in perms:
        print(''.join(p))

# Example usage
if __name__ == "__main__":
    print("Histogram:")
    histogram([3, 5, 2])

    print("\nReversed sentence:")
    print(reverse_sentence("We are ready"))

    print("\nVolume of sphere with radius 3:")
    print(sphere_volume(3))

    print("\nIs 'madam' a palindrome?")
    print(is_palindrome("madam"))

    print("\nPermutations of 'abc':")
    print_permutations("abc")
