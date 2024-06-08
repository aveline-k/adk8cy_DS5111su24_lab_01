def clean_text(input):
        return ''.join(c.lower() for c in input if c.isalnum() or c.isspace())

def tokenize(input):
        cleaned_text = clean_text(input)
        return cleaned_text.split()

def count_words(input):
        words = tokenize(input)
        return {word: words.count(word) for word in set(words)}
