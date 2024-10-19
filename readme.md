# Codewars Python Solutions

This repository contains Python solutions to various coding challenges from [Codewars](https://www.codewars.com/). Each script in this repository solves a specific problem, with examples provided to demonstrate the solution. As I continue solving more challenges, I'll keep adding them to this repo.

## Table of Contents

- [Filling Missing Data in a List](#filling-missing-data-in-a-list-fill_missingpy)
- [CamelCase Converter](#camelcase-converter-camelcaseconverterpy)
- [Narcissistic Number Checker](#narcissistic-number-checker-isnarcissisticnumberpy)
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