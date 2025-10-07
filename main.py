#!/bin/env python3
from stats import *
import sys



def get_book_text(fp):
  book = open(fp, 'r', encoding='utf-8-sig')
  content = book.read()
  book.close
  return content

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book = get_book_text(sys.argv[1])
  num_words = count_words(book)
  num_chars = count_chars(book)
  sorted_letters = sorted_count(num_chars)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for numcount in sorted_letters:
  	print(f"{numcount['char']}: {numcount['num']}")

main()
