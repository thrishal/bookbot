def main(): 
    with open("books/frank.txt") as f:
        file_contents = f.read().lower()
        #print(file_contents)
        word_c = file_contents.split()
        

        letter_c = {}

        for char in file_contents:
            if char.isalpha():
                if char in letter_c:
                    letter_c[char] += 1
                else:
                    letter_c[char] = 1
            
    

        print("--- Begin report of books/frankenstein.txt ---")
        print(len(word_c), " words found in the book\n")
       
        for char, char_count in letter_c.items():
            print(f"The {char} character was found {char_count} times\n")


main()

