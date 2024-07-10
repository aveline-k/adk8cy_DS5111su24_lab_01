# tests/test_clean_text.py
import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(current_dir, os.pardir))
src_dir = os.path.join(repo_root, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from adk8cy.tokenizer import clean_text

def test_clean_text():
    # Given a string with punctuation and mixed case
    text = "But the Raven, sitting lonely on the placid bust, spoke only."
    # When passed to clean_text
    result = clean_text(text)
    # Then it should return lowercase text with no punctuation
    assert result == "but the raven sitting lonely on the placid bust spoke only"
