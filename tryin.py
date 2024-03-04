def reverse_words_order_and_swap_cases(sentence : str):
    strings = sentence.split(" ")
    new = ""
    for j in strings[::-1]:
        for i in j:
            if i.isupper():
                new += i.lower()
            elif i.islower():
                new += i.upper()
        new += " "

    return new

print(reverse_words_order_and_swap_cases("aWESOME is cODING"))


def missingCharacters(s : str):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    alpha = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    for i in set(s):
        if i in nums:
            nums.remove(i)
        if i in alpha:
            alpha.remove(i)
    
    return "".join(nums + alpha)

print(missingCharacters("7985interdisciplinary12"))
