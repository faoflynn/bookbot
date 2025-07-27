from stats import count_words, count_letters, sort_letters
def get_book_text(filepath):
    filecontent = ""
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent

def main():
    book_url = "books/frankenstein.txt"
    book = get_book_text(book_url)
    num_words = count_words(book)
    #print(f"{num_words} words found in the document")
    letter_count = count_letters(book)
    #print(letter_count)

main()
