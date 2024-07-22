# adk8cy_DS5111su24_lab_01
## LAB 1: DS 5111 Data Engineering Fall 2023

## Word Processor

This project contains functions to process text: `clean_text`, `tokenize`, and `count_words`.

- **clean_text**: Removes punctuation and converts text to lowercase.
- **tokenize**: Splits text into words.
- **count_words**: Returns a dictionary with word frequencies.

### Example

```python
text = "But the Raven, sitting lonely on the placid bust, spoke only."
print(count_words(text))
