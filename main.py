from stats import count_words, count_letters, sort_letters
def get_book_text(filepath):
    filecontent = ""
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent

def print_report(book_url, num_words, list_of_letters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_url}...")
    print("----------- Word Count ---------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in list_of_letters:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

def main():
    book_url = "books/frankenstein.txt"
    book = get_book_text(book_url)
    num_words = count_words(book)
    #print(f"{num_words} words found in the document")
    letter_count = count_letters(book)
    #print(letter_count)
    list_of_letters = sort_letters(letter_count)
    print_report(book_url, num_words, list_of_letters)
main()
