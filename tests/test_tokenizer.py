import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# print(f"Current directory: {current_dir}")

repo_root = os.path.abspath(os.path.join(current_dir, os.pardir))
# print(f"Repo root directory: {repo_root}")

src_dir = os.path.join(repo_root, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
# print(f"Updated sys.path: {sys.path}")

# print(f"Contents of src directory: {os.listdir(src_dir)}")

import adk8cy as pkg


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
