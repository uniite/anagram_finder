from modules.anagram_finder import extract_anagram_sets


# If running from this module directly, from the command-line...
if __name__ == "__main__":
    # Find all the anagrams in our system's dictionary file
    # (has one word per line, so it works as an iterable, giving one word per iteration)
    count = extract_anagram_sets(open("/usr/share/dict/words"), open("out.txt", "w"))
    # Print out the number of anagram sets found
    print count
