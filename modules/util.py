import string


def remove_punctuation(word):
    """
    Return the given word without any punctuation:

    >>> remove_punctuation("that's cool")
    'thatscool'

    """

    return "".join([c for c in word if c in string.ascii_letters])

def save_anagram_sets(sets, output_file):
    """
    Save the given list of anagram_sets to the specified file or file-like object.
    """

    for s in sets:
        output_file.write(",".join(s) + "\n")
