import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(repo_root)
sys.path.append('./src')

import adk8cy as pkg
from src.adk8cy.tokenizer import clean_text, tokenize, count_words

def test_clean_text():
    assert pkg.clean_text("Hello, World!") == "hello world"
    assert pkg.clean_text("It's a test.") == "its a test"

def test_tokenize():
    assert pkg.tokenize("hello world") == ["hello", "world"]
    assert pkg.tokenize("its a test") == ["its", "a", "test"]

def test_count_words():
    assert pkg.count_words("hello world hello") == {"hello": 2, "world": 1}
    assert pkg.count_words("its a test its a") == {"its": 2, "a": 2, "test": 1}

if __name__ == "__main__":
    pytest.main()
