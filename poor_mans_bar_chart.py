"""The script maps letters from a string into a dictionary.

Then in prints a bar chart of frequencies.

"""
import sys
import pprint

from collections import Counter


print("\n")
print("The program returns a simple bar chart for the letters"
      "of your sentence.")


while True:

    original = input("What would you like to analize? \n\n")
    print("\n")

    #Remove all non-alphabetic symbols from the input sentence
    SENTENCE = ''.join(filter(str.isalpha, original))
    SENTENCE = SENTENCE.lower()

    pp = pprint.PrettyPrinter(width = 110)

    if len(SENTENCE) > 0:
        print("Lets play!")

        #Count the number of all the symbols in the sentence
        count = Counter(SENTENCE)

        #Convert values into multiple repetition strings
        bar_chart = {k:[k]*v for (k,v) in count.items()}

        pp.pprint(bar_chart)

    else:

        print("The format is incorrect. Please, make sure you used at",
              "least one letter of the alphabet.", file = sys.stderr)

    try_again = input("\n\n\nTry again? (Press ENTER else N to quit.) \n")
    if try_again.lower() == "n":
        sys.exit()
