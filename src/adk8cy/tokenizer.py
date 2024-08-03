"""
Module for text processing: cleaning, tokenizing, and counting words.
"""

import logging
import sys

sys.path.append('./src')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(input_text):
    """
    Cleans text.
    """
    assert isinstance(input_text, str), "Input must be a string."
    cleaned_text = ''.join(char.lower() for char in input_text if char.isalnum() or char.isspace())
    assert isinstance(cleaned_text, str), "Output of clean_text should be a string."
    logging.debug("Cleaned text: %s", cleaned_text)
    return cleaned_text

def tokenize(input_text):
    """
    Splits into tokens.
    """
    cleaned_text = clean_text(input_text)
    tokens = cleaned_text.split()
    assert isinstance(tokens, list), "Output of tokenize should be a list."
    logging.debug("Tokens: %s", tokens)
    return tokens

def count_words(input_text):
    """
    Counts total tokens in text.
    """
    words = tokenize(input_text)
    word_count = {word: words.count(word) for word in set(words)}
    assert isinstance(word_count, dict), "Output of count_words should be a dictionary."
    logging.debug("Word count: %s", word_count)
    return word_count

if __name__ == "__main__":
    SAMPLE_TEXT = "Hello world! I go to UVA, and I'm a student."
    logging.info("Starting text processing")
    CLEANED = clean_text(SAMPLE_TEXT)
    logging.info("Cleaned text: %s", CLEANED)
    TOKENS = tokenize(SAMPLE_TEXT)
    logging.info("Tokens: %s", TOKENS)
    WORD_COUNTS = count_words(SAMPLE_TEXT)
    logging.info("Word counts: %s", WORD_COUNTS)
