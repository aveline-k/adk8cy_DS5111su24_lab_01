
# tests/test_file_processing.py
import sys
import pytest
from tokenizer import clean_text, tokenize, count_words
import os

def read_file(file_name):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, file_name)
    with open(file_path, 'r') as file:
        return file.read()

@pytest.mark.parametrize("file_name", [
    "book_17192.txt",  # The Raven
    "book_932.txt",    # The Fall of the House of Usher
    "book_1063.txt",   # The Cask of Amontillado
    "book_14082.txt"   # Le Corbeau
])

def test_clean_text_file(file_name):
    # Given the contents of a file
    text = read_file(file_name)
    # When passed to clean_text
    result = clean_text(text)
    # Then it should return cleaned text without special characters
    assert isinstance(result, str)

def test_tokenize_file():
    # Given the contents of "The Raven"
    text = read_file("book_17192.txt")
    # When passed to tokenize
    result = tokenize(text)
    # Then it should return a list of words
    assert isinstance(result, list)

def test_count_words_file():
    # Given the contents of "The Raven"
    text = read_file("book_17192.txt")
    # When passed to count_words
    result = count_words(text)
    # Then it should return a dictionary of word counts
    assert isinstance(result, dict)

def test_all_files():
    # Given a list of file paths
    files = ["book_17192.txt", "book_932.txt", "book_1063.txt", "book_14082.txt"]
    combined_text = " ".join([read_file(f) for f in files])

    # When passed to each function
    cleaned = clean_text(combined_text)
    tokens = tokenize(combined_text)
    counts = count_words(combined_text)
    
    # Then ensure the outputs are valid
    assert isinstance(cleaned, str)
    assert isinstance(tokens, list)
    assert isinstance(counts, dict)

french_text = """_Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"""

def test_clean_text_french():
    cleaned = clean_text(french_text)
    assert isinstance(cleaned, str)

def test_tokenize_french():
    tokens = tokenize(french_text)
    assert isinstance(tokens, list)

def test_count_words_french():
    counts = count_words(french_text)
    assert isinstance(counts, dict)

@pytest.mark.skip(reason="Japanese text test not implemented yet")
def test_japanese_text():
    assert False


@pytest.mark.skipif(sys.platform != "linux", reason="Only runs on Linux")
def test_linux_only():
    assert True

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_python_version():
    assert True 

def test_bash_comparison():
    text = "But the Raven, sitting lonely on the placid bust, spoke only."
    result = count_words(text.lower())
    bash_result = os.popen(f"echo '{text}' | tr -d '[:punct:]' | tr ' ' '\\n' | sort | uniq -c").read()

    bash_counts = {}
    for line in bash_result.strip().split('\n'):
        count, word = line.strip().split()
        bash_counts[word.lower()] = int(count)

    assert result == bash_counts

