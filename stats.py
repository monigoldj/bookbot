# Description: This function is intended to read the content of a book file
def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        # Read the content of the file and return it
        book_text = f.read()
    return book_text


def get_words_count(book_text):
    # Count the number of words in the book text
    words_count = book_text.split()
    return len(words_count)


def get_character_count_by_letter(book_text):
    # Count the number of each letter in the book text
    letter_counts = []

    for char in book_text:
        if char.isalpha():
            char = char.lower()
            for entry in letter_counts:
                if entry['letter'] == char:
                    entry['num'] += 1
                    break
            else:
                letter_counts.append({'letter': char, 'num': 1})

    return letter_counts


def sort_on(entry):
    return entry['num']


def sort_letter_count(letter_count_dict):
    return sorted(letter_count_dict, key=sort_on, reverse=True)


def get_and_print_report(filepath):
    book_text = get_book_text(filepath)
    words_count = get_words_count(book_text)
    letter_count_dict = get_character_count_by_letter(book_text)    
    CYAN = '\033[96m'
    RESET = '\033[0m'

    print(f"{CYAN}============ BOOKBOT ============{RESET}")
    print(f"Analyzing book found at {filepath}...")
    print(f"{CYAN}----------- Word Count ----------{RESET}")
    print(f"Found {words_count} total words")
    print(f"{CYAN}--------- Character Count -------{RESET}")
    letter_count_dict_sorted = sort_letter_count(letter_count_dict)
    for entry in letter_count_dict_sorted:
        print(f"{entry['letter']}: {entry['num']}")
        
    return None