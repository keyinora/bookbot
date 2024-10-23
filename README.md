
# Character Frequency Analysis of Text Files

## Overview
This Python script reads a text file, counts the number of words and the frequency of each alphabetic character, and generates a report. The report displays the total number of words and the occurrence of each character sorted in descending order of frequency.

## Purpose
The purpose of this script is to provide a basic analysis of the text, showing both the total number of words and the frequency of each character. It is particularly useful for understanding the distribution of characters in a given text, such as a book.

## How It Works
The script performs the following tasks:

1. Reads the text file specified in `book_path`.
2. Counts the total number of words in the text.
3. Counts the frequency of each alphabetic character in the text (ignoring case).
4. Prints a report showing the total number of words and a list of character frequencies.

## File Structure
```
📂 books/
  └── frankenstein.txt
README.md
main.py
```
The text file `frankenstein.txt` should be placed inside the `books` folder. You can replace this file with any other text file for analysis.

## Script Breakdown

### `main()`
This is the entry point of the script. It defines the path to the text file, processes the text to obtain word and character counts, and prints a report.

### `get_book_text(path)`
- **Input:** A file path.
- **Output:** Returns the contents of the file as a string.
- **Functionality:** Reads the entire text from the file located at the given path and returns it as a string.

### `get_num_words(text)`
- **Input:** A string of text.
- **Output:** Returns an integer representing the number of words.
- **Functionality:** Splits the text into words using whitespace as the delimiter and counts them.

### `count_characters(text)`
- **Input:** A string of text.
- **Output:** Returns a dictionary with characters as keys and their counts as values.
- **Functionality:** 
  - Converts the input text to lowercase.
  - Initializes an empty dictionary to store character counts.
  - Iterates over each character in the text.
  - Counts only alphabetic characters (`a-z`) and ignores non-alphabetic characters.
  - If a character is already in the dictionary, increments its count; otherwise, initializes it with a count of 1.

### `print_report(text, char_count)`
- **Input:** A string of text and a dictionary of character counts.
- **Output:** Prints a report to the console.
- **Functionality:** 
  - Prints the total number of words in the document.
  - Converts the character dictionary into a list of dictionaries and sorts it by character frequency in descending order.
  - Iterates over the sorted list and prints the character along with its count.
  - Displays the beginning and end of the report using separators.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Script
1. Clone the repository or download the script.
2. Place the text file (e.g., `frankenstein.txt`) in the `books/` folder.
3. Run the script:

   ```bash
   python main.py
   ```

### Output Example
```
--- Begin report of books/frankenstein.txt ---
7562 words found in the document

The 'e' character was found 5678 times
The 't' character was found 4532 times
The 'a' character was found 3984 times
...
--- End report ---
```

## Customization
- You can replace `books/frankenstein.txt` with any text file you wish to analyze.
- To change the file path, update the `book_path` variable in the `main()` function.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or additional features!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
