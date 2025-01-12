
def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    word_count = get_word_count(file_contents)
    chars_dict = get_chars_dict(file_contents)
    print_report(path_to_file, word_count, chars_dict)

def get_book_text(path):
    """Returns the content of a File as one String"""
    with open(path) as f:
        return f.read()

def get_word_count(text:str) -> int:
    """Returns the numer of words in a givens String"""
    return len(text.split())

def get_chars_dict(text:str) -> dict:
    """Returns the number each Character in a String (Case Ignored)"""
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
    # Eigene Lösung: Problem hier war das nur die Chars gesucht und gezählt wurden, welche vorher definiert wurden 
    # (Wobei im nächsten Step dann doch mit ".isalpha()" aufs alphabet begrenzt wird)
    # tmp_text = text.lower()
    # result:dict = {}

    # chars = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    # for char in chars:
    #     result[char] = tmp_text.count(char)
    #     print(f"{char} is times {result[char]} in the text")
    
    # return result

def print_report(path, words:int, chars:dict) -> None:
    """Prints out a Report"""
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print("")


    #print Char counts in order
    list_of_char = []
    for char in chars.keys():
        list_of_char.append( (char, chars[char]) )

    list_of_char.sort(reverse=True, key=sort_on)

    for char in list_of_char:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")

def sort_on(tuple):
    """Sort on second value in a tuple"""
    return tuple[1]

if __name__ == "__main__":
    main()