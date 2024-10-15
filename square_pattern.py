# 3 3 3 3 3 
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3 
# 3 3 3 3 3

# Function to print the pattern
def print_pattern(n):
    for i in range(n):
        for j in range(n):
            print(max(abs(n//2 - i), abs(n//2 - j)) + 1, end="")
        print()

# Set n = 9 (size of the pattern)
n = 5
print_pattern(n*2 -1)
