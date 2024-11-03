# Problem Solving using Python

This folder contains Python solutions to various coding challenges from [Codewars](www.codewars.com/r/ykU6Dg). Each script in this repository solves a specific problem, with examples provided to demonstrate the solution.

## Table of Contents

- [Filling Missing Data in a List](#1-filling-missing-data-in-a-list-fill_missingpy)
- [CamelCase Converter](#2-camelcase-converter-camelcaseconverterpy)
- [Narcissistic Number Checker](#3-narcissistic-number-checker-isnarcissisticnumberpy)
- [Remove Vowels from String](#4-remove-vowels-from-string-removevowlespy)
- [Sort Digits in Descending Order](#5-sort-digits-in-descending-order-sortdigitspy)
- [Square Every Digit](#6-square-every-digit-squaredigitspy)
- [Array Difference](#7-array-difference-arraydiffpy)
- [Cake Count](#8-cake-count-cakescountpy)
- [Vowel and Consonant Palindrome](#9-vowel-and-consonant-palindrome-vowlconsonantpalindromepy)
- [Persistent Bugger](#10-persistent-bugger-persistentbuggerpy)
- [Consecutive Strings](#11-consecutive-strings-consecutivestringspy)
- More solutions to come...

---

## 1. Filling Missing Data in a List (`fill_missing.py`)

### Problem Description
You are given a list that may contain missing data represented as `None`, and an integer representing the method to fill the missing data. The list contains only integers and `None` values.

#### Fill Methods:
- `-1`: Replace `None` with the nearest value on the **right** (backward filling).
- `0`: Replace `None` with the **nearest** value (choose the smallest if equally distant).
- `1`: Replace `None` with the nearest value on the **left** (forward filling).

### Example
```python
arr = [None, 1, None, None, None, 2, None]
print(fill(arr, -1))  # Output: [1, 1, 2, 2, 2, 2, None]
print(fill(arr,  0))  # Output: [1, 1, 1, 1, 2, 2, 2]
print(fill(arr,  1))  # Output: [None, 1, 1, 1, 1, 2, 2]
```

## 2. CamelCase Converter (CamelCaseConverter.py)

### Problem Description
Convert a dash (-) or underscore (_) delimited string into camel case. The first word remains unchanged, while the subsequent words are capitalized.

### Example
```python
print(to_camel_case("the-stealth-warrior"))  # Output: "theStealthWarrior"
print(to_camel_case("The_Stealth_Warrior"))  # Output: "TheStealthWarrior"
```

## 3. Narcissistic Number Checker (isNarcissisticNumber.py)

### Problem Description
A Narcissistic number (or Armstrong number) is a number that is equal to the sum of its digits, each raised to the power of the number of digits. The task is to check if a given number is Narcissistic.

### Example

```python
print(narcissistic(153))  # Output: True
print(narcissistic(1652)) # Output: False
```

## 4. Remove Vowels from String (removeVowles.py)

### Problem Description
Trolls are attacking your comment section! A common way to deal with this situation is to remove all the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and returns a new string with all vowels removed.

### Example

```python
print(disemvowel("This website is for losers LOL!"))  
# Output: "Ths wbst s fr lsrs LL!"
```

Note: For this kata, 'y' isn't considered a vowel.

## 5. Sort Digits in Descending Order (`sortDigits.py`)

### Problem Description
Create a function that takes any non-negative integer as input and returns the integer with its digits rearranged in descending order to form the highest possible number.

### Example
```python
print(descending_order(42145))     # Output: 54421
print(descending_order(145263))    # Output: 654321
print(descending_order(123456789)) # Output: 987654321
```

## 6. Square Every Digit (`squareDigits.py`)

### Problem Description
Create a function that squares every digit of a number and concatenates them into a new integer.

### Examples
```python
print(square_digits(9119))  # Output: 811181
print(square_digits(765))   # Output: 493625
```
## 7. Array Difference (`arrayDiff.py`)

### Problem Description
Implement a function that takes two lists, `a` and `b`, and returns a new list where all occurrences of elements from `b` are removed from `a`, while maintaining the original order of `a`.

### Examples
```python
print(array_diff([1, 2], [1]))           # Output: [2]
print(array_diff([1, 2, 2, 2, 3], [2]))  # Output: [1, 3]
```

## 8. Cake Count (`cakesCount.py`)

### Problem Description
Pete wants to bake cakes using specific recipes and available ingredients. Write a function `cakes()` that determines how many cakes Pete can bake with the given recipe and available ingredients. If any required ingredient is missing, it should be considered as 0.

### Examples
```python
# Output: 2
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))

# Output: 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))
```

## 9. Vowel and Consonant Palindrome (`vowlConsonantPalindrome.py`)

### Problem Description
Given a string, check if the sequence of vowels and consonants (separately) are the same forwards and backwards (palindromic). The function should:
- Be case-insensitive
- Ignore spaces, numbers, and special characters
- Treat the letter Y as a consonant
- Return "vowel" if only the vowels are palindromic, "consonant" if only the consonants are palindromic, "both" if both are palindromic, or "neither" if neither are palindromic.

### Examples
```python
# Output: "both"
print(palindrome("egg"))

# Output: "both"
print(palindrome("raCe car"))

# Output: "neither"
print(palindrome("wizard"))

# Output: "vowel"
print(palindrome("pea13ce"))

# Output: "both"
print(palindrome(" *73_ ab"))
```

## 10. Persistent Bugger (`PersistentBugger.py`)

### Problem Description
Write a function `persistence` that calculates the multiplicative persistence of a number. The multiplicative persistence of a number is the number of times you must multiply the digits of a number until you reach a single-digit number.

### Examples
```python
# Output: 3 (3*9 = 27, 2*7 = 14, 1*4 = 4)
print(persistence(39))

# Output: 0 (4 is already a single-digit number)
print(persistence(4))

# Output: 4 (9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, 1*2 = 2)
print(persistence(999))

# Output: 2 (2*5 = 10, 1*0 = 0)
print(persistence(25))
```

## 11. Consecutive Strings (`ConsecutiveStrings.py`)

### Problem Description
You are given an array (`strarr`) of strings and an integer `k`. Your task is to return the first longest string consisting of `k` consecutive strings taken in the array.

### Examples
```python
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
k = 2

# Output: "folingtrashy"
print(longest_consec(strarr, k))

# More examples
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))  # Output: "abigailtheta"
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))  # Output: "oocccffuucccjjjkkkjyyyeehh"
print(longest_consec([], 3))  # Output: ""
print(longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))  # Output: "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
```

### Notes
- If n = 0 or k > n or k <= 0, return an empty string "".
- Consecutive strings follow one after another without interruption.

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/codewars-python-solutions.git
```
2. Navigate to the project directory:
```bash
cd codewars-python-solutions
```
3. Run any script:
```bash
python3 filename.py
```

## Contributions
Feel free to fork this repository, submit issues, or create pull requests to add more solutions or improvements.

Stay tuned for more solutions as I continue solving challenges on Codewars!