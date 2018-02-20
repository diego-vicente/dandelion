import nltk

from itertools import dropwhile

# Download and generate CMU dictionary
nltk.download('cmudict')
pronounciation = dict(nltk.corpus.cmudict.entries())


def get_phonemes(word, selection_criteria):
    """Get the phonetic representation of the syllables after the stress.

    :param word: String containing the word.
    :param selection_criteria: Function to filter the selected phonemes.
    :returns: Syllables corresponding to the word.
    :rtype: list

    """
    try:
        key = word.strip().lower()
        ending = dropwhile(lambda x: '1' not in x, pronounciation[key])
        return [p for p in ending if selection_criteria(p)]
    except KeyError:
        return []


def get_perfect_phonemes(word):
    """Get the phonetic representation of the sounds after the stress.

    :param word: String containing the word.
    :returns: Syllables corresponding to the word.
    :rtype: list

    """
    return get_phonemes(word, lambda p: True)


def get_vowel_phonemes(word):
    """Get the phonetic representation of the vowels after the stress.

    :param word: String containing the word.
    :returns: Vowel syllables corresponding to the word.
    :rtype: list

    """
    return get_phonemes(word, lambda p: any(ch.isdigit() for ch in p))


def get_consonant_phonemes(word):
    """Get the phonetic representation of the consonants after the stress.

    :param word: String containing the word.
    :returns: Consonant syllables corresponding to the word.
    :rtype: list

    """
    return get_phonemes(word, lambda p: not any(ch.isdigit() for ch in p))
