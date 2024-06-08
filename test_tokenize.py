from tokenize import clean_text, tokenize, count_words

def test_clean_text():
    assert clean_text("Hello, World!") == "hello world"
    assert clean_text("It's a test.") == "its a test"

def test_tokenize():
    assert tokenize("hello world") == ["hello", "world"]
    assert tokenize("its a test") == ["its", "a", "test"]

def test_count_words():
    assert count_words("hello world hello") == {"hello": 2, "world": 1}
    assert count_words("its a test its a") == {"its": 2, "a": 2, "test": 1}

if __name__ == "__main__":
    pytest.main()
