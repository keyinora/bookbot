def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    print_report(text, char_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Initialize an empty dictionary to hold character counts
    char_count = {}

    # Iterate through each character in the text
    for char in text:
        # Only count alphabetic characters
        if char.isalpha():
            # Check if the character is already a key in the dictionary
            if char in char_count:
                # If it is, increment its count
                char_count[char] += 1
            else:
                # If not, add it to the dictionary with a count of 1
                char_count[char] = 1
    return char_count

def print_report(text, char_count):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{get_num_words(text)} words found in the document\n")    
    # Convert dictionary to a list of tuples and sort by the number of occurrences
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)    
    # Print sorted character counts
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    
    print(f"--- End report ---")
    
main()