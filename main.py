
def read_book(filename):
    with open(filename) as f:
        book_contents = f.read()
    return book_contents


def count_words(book_contents):
    counter = 0

    for word in book_contents.split():
        counter += 1

    return counter


def count_characters(book_contents):
    char_dict = {}
    for char in book_contents:
        c = char.lower()
        if not char.isalpha():
            continue
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return char_dict


def create_report(cnt_chars, cnt_words, filename):
    sorted_dict = {k: v for k, v in sorted(cnt_chars.items(), key=lambda item: item[1], reverse=True)}
    
    print(f"--- Begin report of {filename} ---")
    print(f"{cnt_words} words found in the document")
    print("")
    
    for k, v in sorted_dict.items():
        print(f"The '{k}' character was found {v} times")

    print("--- END REPORT ---")
filename = 'books/frankenstein.txt'

book_contents = read_book(filename)
cnt_words = count_words(book_contents)
cnt_char = count_characters(book_contents)

create_report(cnt_char, cnt_words, filename)
