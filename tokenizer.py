import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(input_text):
    assert isinstance(input_text, str), "Input must be a string."
    
    cleaned_text = ''.join(char.lower() for char in input_text if char.isalnum() or char.isspace())
    
    assert isinstance(cleaned_text, str), "Output of clean_text should be a string."
    logging.debug(f"Cleaned text: {cleaned_text}")
    
    return cleaned_text

def tokenize(input_text):
    cleaned_text = clean_text(input_text)
    tokens = cleaned_text.split()
    
    assert isinstance(tokens, list), "Output of tokenize should be a list."
    logging.debug(f"Tokens: {tokens}")
    
    return tokens

def count_words(input_text):
    words = tokenize(input_text)
    word_count = {word: words.count(word) for word in set(words)}
    
    assert isinstance(word_count, dict), "Output of count_words should be a dictionary."
    logging.debug(f"Word count: {word_count}")
    
    return word_count

if __name__ == "__main__":
    sample_text = "Hello world! I go to UVA, and I'm a student."
    logging.info("Starting text processing")
    
    cleaned = clean_text(sample_text)
    logging.info(f"Cleaned text: {cleaned}")
    
    tokens = tokenize(sample_text)
    logging.info(f"Tokens: {tokens}")
    
    word_counts = count_words(sample_text)
    logging.info(f"Word counts: {word_counts}")
