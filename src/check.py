from phonetic import get_consonant_sounds, get_perfect_sounds, get_vowel_sounds


def _rhyme(word_a, word_b, sounds_func):
    """Return whether two words form a rhyme.

    This function is just a general version and the shorthands available in the
    same module should be used instead, except a custom function for extracting
    phonemes is to be used.

    :param word_a: first word.
    :param word_b: second word.
    :param sounds_func: function to extract relevant phonemes.

    :returns: True if they rhyme following the given conditions.

    :rtype: bool
    """
    sounds_a = sounds_func(word_a)
    sounds_b = sounds_func(word_b)
    return sounds_a == sounds_b


def perfect_rhyme(word_a, word_b):
    """Return whether two words form a perfect rhyme.

    :param word_a: first word.
    :param word_b: second word.
    :returns: True if they perfectly rhyme.
    :rtype: bool

    """
    return _rhyme(word_a, word_b, get_perfect_sounds)


def vowel_rhyme(word_a, word_b):
    """Return whether two words form a vowel rhyme.

    :param word_a: first word.
    :param word_b: second word.
    :returns: True if they rhyme on vowels.
    :rtype: bool

    """
    return _rhyme(word_a, word_b, get_vowel_sounds)


def consonant_rhyme(word_a, word_b):
    """Return whether two words form a consonant rhyme.

    :param word_a: first word.
    :param word_b: second word.
    :returns: True if they rhyme on consonants.
    :rtype: bool

    """
    return _rhyme(word_a, word_b, get_consonant_sounds)
