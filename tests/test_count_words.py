# tests/test_count_words.py

import pytest
from tokenizer import count_words

def test_count_words():
    # Given a string with repeated words
    text = "But the Raven, sitting lonely on the placid bust, spoke only."
    # When passed to count_words
    result = count_words(text)
    # Then it should return a dictionary with word counts
    expected = {"but": 1, "the": 2, "raven": 1, "sitting": 1, "lonely": 1, "on": 1, "placid": 1, "bust": 1, "spoke": 1, "only": 1}
    assert result == expected
