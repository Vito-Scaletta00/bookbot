def main():
    print("--- Begin report of books/frankenstein.txt ---")
    wordcount = count_words()
    print(wordcount, "words found in the document")
    print("")
    character_dict = count_characters()
    sorted_characters = sort_dict(character_dict)
    print_sorted_characters(sorted_characters)
    print("--- End report ---")

def book_read():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    wordcount = 0
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
        booksplit = book_contents.split()
        for word in booksplit:
            wordcount += 1
        return(wordcount)

def count_characters():
    with open("books/frankenstein.txt") as book:
        book_string = book.read()
        lowered_string = book_string.lower()
        character_dict = {}
        character_count = 0
        for character in lowered_string:
            if character.isalpha():
                if character not in character_dict:
                    character_dict[character] = 1
                else:
                    character_dict[character] += 1
        return character_dict
    
def convert_dict_to_list(character_dict):
    character_list = []
    for char, count in character_dict.items():
        character_list.append({"character":char, "num": count})
    return character_list

def sort_on(character_dict):
    return character_dict["num"]

def sort_dict(character_dict):
    character_list = convert_dict_to_list(character_dict)
    character_list.sort(reverse=True, key=sort_on)
    return character_list
    
def print_sorted_characters(sorted_characters):
    for item in sorted_characters:
        print(f"The '{item['character']}' character was found {item['num']} times")



main()



