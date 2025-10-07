def count_words(book):
	return len(book.split())
  
def count_chars(book):
	char_count = {}
	for char in book.lower():
		char_count[char] = char_count.setdefault(char,0) + 1
	return char_count
	
def sort_on(items):
	return items["num"]
	
def sorted_count(char_count):
	count_list = []
	for key, value in char_count.items():
		if key == '\n':
			key = '\\n'
		count_list.append({"char": key, "num": value})
		
	count_list.sort(reverse=True, key=sort_on)
	return count_list
	
	