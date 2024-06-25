# Challenge #2

# IS IT AN ANAGRAM?
# Write a function that takes two words (String) and returns true or false (Bool) depending on whether or not they are anagrams.
# - An Anagram consists of forming a word by rearranging ALL the letters of another initial word.
# - It is NOT necessary to check that both words exist.
# - Two same words are not an anagram.

def anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    word1 = word1.lower()
    word2 = word2.lower()

    return sorted(word1) == sorted(word2)

def main():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    print(anagram(word1, word2))

if __name__ == "__main__":
    main()
