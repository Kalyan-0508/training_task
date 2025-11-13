words = ["apple", "banana", "kiwi", "orange"]   # your list of words
vowels = "aeiouAEIOU"

vowel_count = {word: sum(1 for ch in word if ch in vowels) for word in words}

print(vowel_count)

