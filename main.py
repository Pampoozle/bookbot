def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_nb = count_words(text)
    letter_dict = count_letters(text)
    sorted = sort_letters(letter_dict)
    print(f"--- Begin report of {book_path} ---")
    print("*********************************************************************************************")
    print(f"{word_nb} words are found in this text")
    print("*********************************************************************************************")
    for letter, count in sorted:
        print(f"The {letter} character was found {count} times")
    print("*********************************************************************************************")
    print("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict = {}
    lower_case = text.lower()
    for character in lower_case:
        if character.isalpha():
            if character in letter_dict:
                letter_dict[character] += 1
            else:
                letter_dict[character] = 1
    return letter_dict
            
def sort_letters(letter_dict):
    letter_list = [(key,value) for key, value in letter_dict.items()]
    letter_list.sort(reverse=True, key=lambda x:x[1])
    return letter_list

if __name__ == "__main__":
    main()