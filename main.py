def main(): 
    with open("books/frank.txt") as f:
        file_contents = f.read()
        print(file_contents)

main()

