text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
symbols = 0
words = 0

# Count words
words = len(text.split())

for ch in text:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch != ' ':
        symbols += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Words:", words)
print("Symbols:", symbols)
