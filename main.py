def main():
    with open(r"./books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

def count_words(book_path : str) -> int:
    with open(book_path) as book:
        file_contents = book.read()
    count: int = 0
    for word in file_contents.split():
        count += 1
    return count

def count_characters(book_path : str) -> int:
    with open(book_path) as book:
        file_contents: str = book.read()
    count: dict = {}
    for character in file_contents.lower():
        if character not in count:
            count.update({character:file_contents.count(character)})
    return sorted(count.items())


# words = count_words(r"./books/frankenstein.txt")
# print(words)

a = count_characters(r"./books/frankenstein.txt")
print(a)