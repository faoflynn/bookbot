def get_book_text(filepath):
    filecontent = ""
    with open(filepath) as f:
        filecontent = f.read()
    return filecontent

def countWords(text):
    words = text.split()
    return len(words)

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = countWords(book)
    print(f"{num_words} words found in the document")

main()
