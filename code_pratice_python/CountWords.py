'''write a python program to count the number of words in a given string.'''
from collections import Counter


def frequency1(input_string):
    """Return a dictionary mapping words to their frequency in the string.

    Splits on any whitespace and is case-sensitive.
    """
    words = input_string.split()
    return dict(Counter(words))

############################################################################

def count_words():
    input_string = input("Enter a string: ")
    freq = frequency1(input_string)
    for word, cnt in freq.items():
        print(word, cnt)

#############################################################################

def frequency3(String1):
    list_word = String1.split(' ')
    frequency = {}
    
    for word in list_word:
        count = frequency.get(word)
        if count is None:
            frequency[word]= 1
        else:
            frequency[word] = count + 1
    
    for key, value in frequency.items():
        print(key,  value)

String1 = "I am am learning learning java java java programming"

print(frequency1(String1))

################################################################################

if __name__ == "__main__":
    # Example usage
    String1 = "I am am learning learning java java java programming"
    print(frequency1(String1))
