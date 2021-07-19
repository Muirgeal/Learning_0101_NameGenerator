"""Turn an input word into its Pig Latin equivalent."""

import sys

print("\n")
print("Welcome to 'Pig Latin Translator' \n")

VOWELS = 'aeiou'

while True:

    original = input("What word would you like to translate? \n")
    print("\n")

    #Remove white space from the beginning and the end
    original = original.strip()

    if len(original) > 0 and original.isalpha():

        word = original.lower()

        first = word[0]

        if first in VOWELS:
            result = word + "way"
            print(result, file = sys.stderr)
        else:
            result = word[1:] + first + "ay"
            print(result, file = sys.stderr)

    else:
        print("The format is incorrect. Please, make sure you entered a word",
              "consisting of alphabetic characters only.", file = sys.stderr)

    try_again = input("\n\n\nTry again? (Press ENTER else N to quit.) \n")
    if try_again.lower() == "n":
        sys.exit()
