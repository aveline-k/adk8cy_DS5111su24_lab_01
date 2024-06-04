default:
	cat Makefile

get_texts:
	wget https://www.gutenberg.org/cache/epub/17192/pg17192.txt -O raven.txt

raven_line_count:
	wc -l raven.txt

raven_word_count:
	wc -w raven.txt

raven_counts:
	grep -o -i 'raven' raven.txt | wc -l
	grep -o 'Raven' raven.txt | wc -l
	grep -o -i 'raven' raven.txt | wc -l

total_lines:
	wc -l *.txt

total_words:
	wc -w *.txt

clean:
	rm -f raven.txt
