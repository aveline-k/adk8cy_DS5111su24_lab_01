# tests/test_clean_text.py

import pytest
from tokenizer import clean_text

def test_clean_text():
    # Given a string with punctuation and mixed case
    text = "But the Raven, sitting lonely on the placid bust, spoke only."
    # When passed to clean_text
    result = clean_text(text)
    # Then it should return lowercase text with no punctuation
    assert result == "but the raven sitting lonely on the placid bust spoke only"
