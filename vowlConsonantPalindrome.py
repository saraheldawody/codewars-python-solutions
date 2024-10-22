"""
Given a string, we'd like to know whether the vowels, consonants or both (assessed separately) are the same backwards as they are forwards. See examples at the bottom of this description.

The test should be case-insensitive, and should only assess letters, ignoring spaces, numbers and other non-letter characters ("_" "*" " " "-"). Vowels are AEIOU. The letter Y is a consonant for this exercise.

If the string doesn't have the same sequence of consonants or vowels backwards, we want to return "neither". If only the vowels are palindromic, return "vowel". If only the consonants are palindromic, return "consonant". If the vowels and the consonants in the string are palindromic, return "both".

You can assume that all test cases will contain at least one vowel and one consonant.

Enjoy!

Some examples:

"egg" would return "both", as "e" is the same backwards as it is forwards, as is "gg".

"raCe car" would also return "both" as "rccr" and "aea" are palindromes.

"wizard" would return "neither".

"pea13ce" would return "vowel" as "eae" is palindromic, but "pc" is not.

" *73_ ab" would return "both" as "a" and "b" are palindromic (according to me...)
"""

def palindrome(s):
    vowls='aeiou'
    consonants='bcdfghjklmnpqrstvwxyz'
    s=s.lower()
    s_vowls=''
    s_consonants=''
    for l in s:
        if l in vowls:
            s_vowls+=l
        if l in consonants:
            s_consonants+=l
    is_vowl_palindrom=s_vowls==s_vowls[::-1]
    is_consonants_palindrom=s_consonants==s_consonants[::-1]
    if is_vowl_palindrom and is_consonants_palindrom:
        return "both"
    elif is_vowl_palindrom:
        return 'vowel'
    elif is_consonants_palindrom:
        return 'consonant'
    else:
        return 'neither'
    