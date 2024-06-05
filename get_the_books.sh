#!/bin/bash

book_ids=(17192 32037 932 1064 10947 1063 51060 2147 2151 2150 2148)

for id in "${book_ids[@]}"
do
    wget "https://www.gutenberg.org/cache/epub/$id/pg$id.txt" -O "book_$id.txt"
done
