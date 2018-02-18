from phonetic import get_consonant_sounds, get_perfect_sounds, get_vowel_sounds


def perfect_rhyme(word_a, word_b):
    """Return whether two words form a perfect rhyme.

    :param word_a: first word.
    :param word_b: second word.
    :returns: True if they perfectly rhyme.
    :rtype: bool

    """
    sounds_a = get_perfect_sounds(word_a)
    sounds_b = get_perfect_sounds(word_b)
    return sounds_a == sounds_b


def vowel_rhyme(word_a, word_b):
    """Return whether two words form a vowel rhyme.

    :param word_a: first word.
    :param word_b: second word.
    :returns: True if they rhyme in vowels.
    :rtype: bool

    """
    sounds_a = get_vowel_sounds(word_a)
    sounds_b = get_vowel_sounds(word_b)
    return sounds_a == sounds_b


def consonant_rhyme(word_a, word_b):
    """Return whether two words form a consonant rhyme.

    :param word_a: first word.
    :param word_b: second word.
    :returns: True if they rhyme in consonants.
    :rtype: bool

    """
    sounds_a = get_consonant_sounds(word_a)
    sounds_b = get_consonant_sounds(word_b)
    return sounds_a == sounds_b
