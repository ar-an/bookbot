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
    count_dict: dict[str: int] = {}
    for character in file_contents:
        if character.lower() not in count_dict and character.isalpha() and character.islower():
            count_dict.update({character:file_contents.lower().count(character)})
    return sorted(count_dict.items())

def report_char(book_path:str) -> int:
    with open(book_path) as book:
        book_contents: str = book.read()
    count_dict: dict[str: int] = {}
    for character in book_contents:
        if character.lower() not in count_dict and character.isalpha() and character.islower():
            count_dict.update({character:book_contents.lower().count(character)})
    report = f"""--- Begin report of {book_path} --- '\n' 
    {count_words(book_path)} words found in document '\n'"""
    for char in sorted(count_dict.items()):
        report += f"The {char[0]} character was found {char[1]} times'\n'"
    report += "--- End report ---"
    return report.replace("'", "")

book_path: str = r"./books/frankenstein.txt"


# words = count_words(r"./books/frankenstein.txt")
# print(words)

# char = count_characters(r"./books/frankenstein.txt")
# print(char)

report = report_char(book_path=book_path)
print(report)