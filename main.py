with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def words(file):
    words = file.split()
    print()
    print(len(words))
    print()
    return len(words)

def count_characters(book_text) -> dict:
    book_text = book_text.lower()
    char_count = {}

    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print (char_count)
    print()
    return char_count

def generate_report(file_path):
    with open(file_path, 'r') as file:
        book_text = file.read()
    
    char_count = count_characters(book_text)
    word_count = words(book_text)
    
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(reverse=True, key=lambda x: x["num"])
    
    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    
    print("--- End report ---")


words(file_contents)
count_characters(file_contents)
generate_report('books/frankenstein.txt')