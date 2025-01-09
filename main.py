def main():
    book_path = "books/frankenstein.txt"
    # text = get_book_text(book_path)
    # num_words = word_count(text)
    # chars_dict = char_count(text)
    print(summary_report(book_path))

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

def summary_report(path):
    text = get_book_text(path)
    num_words = word_count(text)
    char_dict = char_count(text)
    char_list = []

    for key in char_dict:
        if key.isalpha():
            char_list.append({"letter": key, "count": char_dict[key]})

    char_list = sorted(char_list, reverse=True, key=lambda x: x["count"])

    report = ""
    title = f"--- Begin report of {path} ---\n"
    word_count_report = f"{num_words} found in the document\n\n"
    report += title
    report += word_count_report

    for i in range(0, len(char_list)):
        char_count_report = f"The '{char_list[i]["letter"]}' character was found {char_list[i]["count"]} times\n"
        report += char_count_report
    report += "--- End of report ---"

    return report

main()
