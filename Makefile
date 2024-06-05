default:
	cat Makefile

get_texts:
	bash get_the_books.sh

raven_line_count:
	wc -l book_17192.txt

raven_word_count:
	wc -w book_17192.txt

raven_counts:
	grep -o -i 'raven' book_17192.txt | wc -l
	grep -o 'Raven' book_17192.txt | wc -l
	grep -o -i 'raven' book_17192.txt | wc -l

total_lines:
	wc -l *.txt

total_words:
	wc -w *.txt

clean:
	rm -f book_17192.txt
