import re
print("Enter the number of cards")
n=int(input())
match = re.compile(r'[456]\d{3}[''-]\d{4}[-'']\d{4}[''-]\d{4}')
for i in range(n):
    print("Valid" if match.search(input()) else "Invalid")

