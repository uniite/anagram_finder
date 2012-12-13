from collections import defaultdict
import string



def remove_punctuation(word):
    """
    Return the given word without any punctuation:

    >>> remove_punctuation("that's cool")
    'thatscool'

    """

    return "".join([c for c in word if c in string.ascii_letters])


def anagram_hash(word, ignore_punc=True):
    """
    Returns a hash of the given word, suitable for checking anagram equality:

    >>> anagram_hash("fiber")
    'befir'
    >>> anagram_hash("brief")
    'befir'

    It ignores character cases, and punctuation by default:

    >>> anagram_hash("It's")
    'ist'
    >>> anagram_hash("sit")
    'ist'

    To consider punctuation as part of the anagram, pass ignore_punc=False

    >>> anagram_hash("it's", ignore_punc=False)
    "'ist"

    """

    # Remove punctuation, if requested
    if ignore_punc:
        word = remove_punctuation(word)
    # Convert the word to lowercase, then sort its letters
    # This gives us a string that will only be equal for words that are anagrams
    return "".join(sorted(word.lower()))


def find_anagrams(dict_file):
    """
    Returns a list of groups of anagrams, from the given dictionary file
    (the file is assumed to have one word per line):

    >>> from StringIO import StringIO
    >>> find_anagrams(StringIO("\\n".join(["fiber", "tire", "tier", "brief", "save"])))
    [['tire', 'tier'], ['fiber', 'brief']]

    """

    # We will store the anagrams in lists in a dict, keyed by hash, for easy aggregation
    anagrams = defaultdict(list)

    # Go through the dict_file one word/line at a time
    for word in dict_file:
        # Make sure we don't get any leading/trailing whitespace
        word = word.strip()
        # Compute the anagram hash we will use to group the anagrams
        word_hash = anagram_hash(word)
        # Skip words with an empty hash (they are either blank strings, or have no anagrams)
        if word_hash == "":
            continue
        # Save our word with it's anagrams, as determined by the word's hash
        anagrams[word_hash].append(word)

    # Return only the groups that have more than one word
    # (ie. exclude words that have no anagrams)
    return [group for group in anagrams.values() if len(group) > 1]


if __name__ == "__main__":
    result = find_anagrams(open("/usr/share/dict/words"))
    for anagrams in result:
        print ", ".join(anagrams)
    print len(result)