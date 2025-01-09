def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = char_count(text)
    print(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(string):
    word_list = string.split()
    return len(word_list)

def char_count(string):
    lowerified = string.lower()
    char_dict = {}

    for char in lowerified:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()
