#Time Complexity = O(n log n)
def anagram():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    if sorted(word1) == sorted(word2):
        print("The words are anagrams.")
    else:
        print("The words are not anagrams.")

if __name__ == "__main__":    anagram()

