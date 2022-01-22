"""EX01 - A cute step toward Wordle."""

__author__ = "730362668"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = (input("Enter a single character: "))
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)

count_matches: int = 0 

if word[0] == character:
    print(character + " found at index " + str(0))
    count_matches = count_matches + 1
if word[1] == character:
    print(character + " found at index " + str(1))
    count_matches = count_matches + 1
if word[2] == character:
    print(character + " found at index " + str(2))
    count_matches = count_matches + 1
if word[3] == character:
    print(character + "found at index " + str(3))
    count_matches = count_matches + 1
if word[4] == character:
    print(character + " found at index " + str(4))
    count_matches = count_matches + 1

if count_matches == 1:
    s = ''
else:
    s = 's'
    if count_matches == 0:
        count_matches = "No"
print(str(count_matches) + " instance" + s + " of " + (character) + " found in " + word)






















