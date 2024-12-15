def bookWordCount(book_contents):
    return (len(book_contents.split()))

def bookCharachterCount(book_contents):
    charachter_count = {}

    for charachter in book_contents:
        charachter = charachter.lower()
        if (charachter not in charachter_count):
            charachter_count[charachter] = 0
        charachter_count[charachter.lower()] += 1
    return charachter_count

def main():
    with open("./books/frankenstein.txt") as book:
        book_contents = book.read()
        print(bookWordCount(book_contents))
        print(bookCharachterCount(book_contents))

main()