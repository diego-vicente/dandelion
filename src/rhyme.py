import nltk

from itertools import dropwhile

# Download and generate CMU dictionary
nltk.download('cmudict')
pronounciation = dict(nltk.corpus.cmudict.entries())


def get_perfect_rhyme(word):
    """Get the phonetic representation of the syllables after the stress.

    :param word: String containing the word.
    :returns: Syllables corresponding to the word.
    :rtype: list

    """
    try:
        ending = dropwhile(lambda x: '1' not in x, pronounciation[word])
        return list(ending)
    except KeyError:
        return []


def get_vowel_rhyme(word):
    """Get the phonetic representation of the vowels after the stress.

    :param word: String containing the word.
    :returns: Vowel syllables corresponding to the word.
    :rtype: list

    """
    try:
        ending = dropwhile(lambda x: '1' not in x, pronounciation[word])
        return [s for s in ending if any(char.isdigit() for char in s)]
    except KeyError:
        return []
