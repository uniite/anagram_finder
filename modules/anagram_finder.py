from collections import defaultdict
from util import remove_punctuation, save_anagram_sets


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

def extract_anagram_sets(words, output):
    """
    Extract all the anagram sets from words, and write the sets to output.

    The words argument can be any iterable set of words, and output must be a file or file-like object.
    The output format is one set per line, with words comma-separated.

    Singletons (words that have no anagrams), punctuation, and letter case are ignored.
    """

    # Find all the anagrams in our system's dictionary file
    # (has one word per line, so it works as an iterable, giving one word per iteration)
    anagram_sets = find_anagrams(words)
    # Sort the sets by size, with the largest sets first
    anagram_sets.sort(key=len, reverse=True)
    # Save the anagram sets to a file named out.txt, one set per line, with the anagrams comma-separated
    save_anagram_sets(anagram_sets, output)
    # Return the number of anagram sets found
    return len(anagram_sets)

def find_anagrams(words, ignore_case=True):
    """
    Returns a list of anagrams sets, from the given iterable set of words:

    >>> find_anagrams(["fiber", "tire", "tier", "brief", "save"])
    [['tire', 'tier'], ['fiber', 'brief']]

    Note: all words are converted to lowercase, such that words of differing case are treated as duplicates:

    >>> find_anagrams(["Tier", "tier", "tire"])
    [['tier', 'tire']]

    """

    # We will store the anagrams in lists in a dict, keyed by hash, for easy aggregation
    anagram_sets = defaultdict(list)

    # Go through the dict_file one word/line at a time
    for w in words:
        # Make sure we don't get any leading/trailing whitespace, and that we're dealing with lowercase words
        w = w.strip().lower()
        # Compute the anagram hash we will use to group the anagrams
        word_hash = anagram_hash(w)
        # Skip words with an empty hash (they are either blank strings, or have no anagrams)
        if word_hash == "":
            continue
        # Save our word with in the matching anagram set, as determined by the word's hash,
        # unless the word is already in the set
        a_set = anagram_sets[word_hash]
        if not w in a_set:
            a_set.append(w)

    # Return only the sets that have more than one word
    # (ie. exclude words that have no anagrams)
    return [group for group in anagram_sets.values() if len(group) > 1]
