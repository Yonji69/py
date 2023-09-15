def display_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i in range(n):
                if i < len(lines):
                    print(lines[i].strip())  # strip() to remove newline characters
                else:
                    break
    except FileNotFoundError:
        print("File not found.")

def find_word_frequency(file_name, word):
    try:
        with open(file_name, 'r') as file:
            content = file.read().lower()
        word_count = content.count(word.lower())
        print(f"The word '{word}' occurs {word_count} times in the file.")
    except FileNotFoundError:
     print("File not found.")
if __name__ == "__main__":
    file_name = input("Enter the file name: ")
# Display the first N lines of the file
    n = int(input("Enter the number of lines to display: "))
    print("\nFirst N lines of the file:")
    display_first_n_lines(file_name, n)
# Find the frequency of a word in the file
    search_word = input("\nEnter a word to find its frequency: ")
    find_word_frequency(file_name, search_word)