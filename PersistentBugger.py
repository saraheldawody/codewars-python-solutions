"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
"""

def persistence(n):
    if len(str(n)) == 1:
        return 0
    else:
        multiplicatives = 0
        num = n
        while len(str(num)) > 1:
            res=1
            for d in str(num):
                res *= int(d)
            multiplicatives += 1
            num = res
        return multiplicatives
    

print("Persistence of 39: ", persistence(39))
print("Persistence of 4: ", persistence(4))
print("Persistence of 999: ", persistence(999))
print("Persistence of 25: ", persistence(25))