def palindrome(a):
    a_reverse = a[::-1]
    return a == a_reverse

print(palindrome('лес'))