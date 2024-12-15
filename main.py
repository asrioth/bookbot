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

def printCharachterCounts(charachter_count):
    for character in charachter_count:
        charachter_count_text = f"The '{character}' appeared {charachter_count[character]} times"
        print(charachter_count_text)

def printBookReport(book_contents, book_path):
    header_text = f"*** Counting report for {book_path} ***"
    footer_text = "*** Counting report end ***"
    word_count = bookWordCount(book_contents)
    word_count_text = f"{word_count} words found in {book_path}"
    charachter_count = bookCharachterCount(book_contents)
    print(header_text)
    print(word_count_text)
    print() #spacer
    printCharachterCounts(charachter_count)
    print(footer_text)

def main():
    frankenstein_path ="books/frankenstein.txt"
    with open(frankenstein_path) as book:
        book_contents = book.read()
        printBookReport(book_contents, frankenstein_path)
        

main()