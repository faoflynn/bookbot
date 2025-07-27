from stats import count_words
def get_book_text(filepath):
    filecontent = ""
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book)
    print(f"{num_words} words found in the document")

main()
