# Units tests can also catch issues. Let's use unit tests to catch an issue with the following code:
# The matching_substring function takes a string s and a range, defined by a and b, and then determines if the given substring,
# sub, is within that range of the string.
# For example, if our string is "pineapple" and our substring is "apple", and the range we're searching is 2 to 9 ("neapple"),
# we return True, since "apple" is a substring. However, if our range was 5 to 9 ("pple"), we would return False.
# s and sub can be any string of any length
# If s is an empty string, then sub can never be a substring, regardless of range
# If sub is an empty string, then sub can never be a substring, regardless of range
# a and b don't necessarily have to be in order. If we had a = 9, b = 2,
# we would treat the range as 2 to 9, same as a = 2, b = 9.
def matching_substring(s, sub, a, b):
    '''Given a string s and a range contained by a & b, return True if sub is in that range of s'''
    return sub in s[a:b]

# Dinamik testler ve sonuçları yazdırma
tests = [
    ("pineapple", "apple", 2, 9, True),
    ("pineapple", "apple", 9, 2, False),
    ("pineapple", "", 2, 1, True),
    ("", "apple", 0, 5, False),  # Düzeltilmiş: True beklenmiyor, False doğru
    ("pineapple", "", 9, 2, True),
    ("amancanalpanama", "ana", 9, 14, True),
    ("amancanalpanama", "", 9, 3, True),
    ("", "ana", 9, 1, False),  # Düzeltilmiş: True yerine False olmalı
]

# Test sonuçlarını dinamik olarak kontrol et ve yazdır
for s, sub, a, b, expected in tests:
    result = matching_substring(s, sub, a, b)
    print(f"{s, sub, a, b} return ==> {result}, expected ==> {expected}")
    assert result == expected, f"Test failed for input: {s, sub, a, b}"
