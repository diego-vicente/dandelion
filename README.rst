===========================================
 ``dandelion`` - Rhyme detection in Python
===========================================

``dandelion`` is a package based on ``nltk`` that allows to detect rhymes in
English. Currently ``dandelion`` is experimental and its functionality has
still to be expanded and tested to be stable. Furthermore, until a stable
version is released, it is expected to suffer breaking changes in the API each
new release.

Currently, the package relies on the Carnegie Mellon University dictionary to
interpret and test for different rhymes. In the future, the aim is to develop a
model able to perform better analysis of rhyme schemes in paragraphs or
stanzas, as well as more general models that are able to cope with words that
do not appear in the CMU dictionary.

Examples
========

Currently, ``dandelion`` offers detection of different types of rhymes.

>>> check.perfect_rhyme('bean', 'green')
True
>>> check.vowel_rhyme('car', 'guard')
True


Installation
============

It is possible to download the latest version of ``dandelion`` using ``pip`` by
running ``pip install dandelion`` or to download one of the versions provided
by GitHub and run ``pip install`` locally.

License
=======

``dandelion`` is licensed under MIT License (available with the source code).
This means that its distribution, use or modification is allowed as long as the
copyright notice is preserved. This includes all purposes including private and
commercial uses.
