def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_character_count(text)
    sorted_counts = sort_counts(char_counts)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char_dict in sorted_counts:
        char = char_dict['char']
        count = char_dict['count']
        print(f"The '{char}' character was found {count} times")
    
    print(f"--- End report  ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def sort_counts(char_counts):
    char_list = [{'char': char, 'count': count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=lambda x: x['count'])
    
    return char_list

main()