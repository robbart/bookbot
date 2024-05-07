# initial configuration of Global items
filename = "books/frankenstein.txt"
char_dict = {}

def main():
    with open(filename) as f:
        file_contents = get_file(f)
        words = split_file(file_contents)
        build_chars_dict(file_contents)
        
        print_report(filename, words)

def get_file(filename):
    file_contents = filename.read()
    return file_contents

def split_file(text):
    return text.split()

def count_words(list):
    return len(list)

def build_chars_dict(text):
    for letter in text:      
        if letter.isalpha():  
            char = letter.lower()

            if char_dict.get(char) == None: 
                char_dict[char] = 1
            else:
                char_dict[char] = char_dict.get(char)+1

def value_getter(item):
    return item[1]

def print_report(filename, words):
    sorted_dict=sorted(char_dict.items(), key=value_getter, reverse=True)
    
    print(f"--- Begin report of {filename} ---")
    print(f"{count_words(words)} words found in the document.\n")

    for letter in sorted_dict:
        print(f"The '{letter[0]}' character was found {letter[1]} times")

    print(f"--- End report ---")

main()