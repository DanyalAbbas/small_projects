def is_palindrome(a):
    if a == a[::-1]:
        return f"{a.upper()} is a palindrome"
    return f"{a.upper()} is not a palindrome"
name = input("Enter anything to see if its palindrome or not : ")
print(is_palindrome(name.lower()))
    