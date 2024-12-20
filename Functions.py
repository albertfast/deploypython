# def my_function(x):
#     print("Hello" + str(x))
# my_function(" world!")  # Hello world!

# def same_lsb(x,y):
#     return x % 2 == y % 2
#
# print(same_lsb(4,5)) # False
# print(same_lsb(1,5)) # True
# print(same_lsb(4,6)) # True

x = "Look to la luna"
rep_a = "a"
rep_b = "e"

def replace_char(s, a, b):
    res = ""
    for c in s:
        if c == a:
            res += b
        else:
            res += c
    return res
print(replace_char(x, rep_a, rep_b)) # Look to le lune
print("Look to la luna".replace("a", "e")) # Look to le lune