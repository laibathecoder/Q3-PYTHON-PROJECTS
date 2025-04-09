

import json 

library: list = []


def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)


def load_library():
    global library
    try:
        with open("library.txt", "r") as file:
            library = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        library = []


def add_book():
    title = input("Please Enter the book title: ")
    author = input("Enter the Author name of the book: ")
    year = int(input("Enter the year of the book: "))
    genre = input("Enter book genre: ")
    read_status = input("Have you read this book (YES/NO): ").strip().lower() == "yes"

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read Status": read_status,
    }

    library.append(book)
    save_library()
    print("Book added successfully! ✔")


def remove_book():
    title = input("Enter the book title to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print(f"'{title}' has been removed successfully from the library.")
            return

    print(f"'{title}' not found in the library.")


def search_book():
    choice = input("Search by (1) Title or (2) Author: ").strip()

    if choice not in ["1", "2"]:
        print("Invalid Choice! Please enter 1 or 2.\n")
        return

    keyword = input("Enter the name of your search term: ").lower()
    results = []

    for book in library:
        if (choice == "1" and keyword in book["Title"].lower()) or (choice == "2" and keyword in book["Author"].lower()):
            results.append(book)

    if results:
        for book in results:
            print(f'Book: {book["Title"]} by Author: {book["Author"]} Year: {book["Year"]} - Genre: {book["Genre"]} - Read Status: {"Read" if book['Read Status'] else "Unread"}')
    else:
        print("No matching book found in the library! 😕")


def display_books():
    if not library:
        print("Library is empty!\n")
        return

    for idx, book in enumerate(library, start=1):
        print(f'{idx}. {book["Title"]} by {book["Author"]} ({book["Year"]}) - {book["Genre"]} - {"Read" if book["Read Status"] else "Unread"}')
    print()


def display_statistics():
    total_books = len(library)
    read_books = 0

    for book in library:
        if book["Read Status"]:
            read_books += 1

    if total_books > 0:
        percentage_read = round((read_books / total_books) * 100, 2)
    else:
        percentage_read = 0

    print(f"Total Books: {total_books}")
    print(f"Read Percentage: {percentage_read}%\n")


def main():
    while True:
        print("\n Welcome to your CLI-based Personal Library Manager! \n")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice please: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye! 😊")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    load_library()
    main()
