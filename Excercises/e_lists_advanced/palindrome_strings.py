words = input().split()
searched_word = input()

palindromes = [element for element in words if element == element [::-1]]

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_word)} times")