import json

books = []
filename = "books.json"

# Stage 1: Data Management

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    genre = input("Enter the book genre: ")
    isbn = input("Enter the book ISBN: ")
    
    book = {
        'title': title,
        'author': author,
        'genre': genre,
        'isbn': isbn
    }
    
    books.append(book)
    print("Book added successfully.")

def update_book():
    title = input("Enter the title of the book to update: ")
    for book in books:
        if book['title'] == title:
            print("Book found. Enter new details:")
            book['title'] = input("Enter the updated title: ")
            book['author'] = input("Enter the updated author: ")
            book['genre'] = input("Enter the updated genre: ")
            book['isbn'] = input("Enter the updated ISBN: ")
            print("Book updated successfully.")
            return
    print("Book not found.")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    for book in books:
        if book['title'] == title:
            books.remove(book)
            print("Book deleted successfully.")
            return
    print("Book not found.")

# Stage 2: Book Search and Display

def search_books():
    keyword = input("Enter a search keyword: ")
    found_books = []
    for book in books:
        if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower() or keyword.lower() in book['genre'].lower() or keyword in book['isbn']:
            found_books.append(book)
    
    if found_books:
        print("Search results:")
        display_books(found_books)
    else:
        print("No books found.")

def display_books(books_list=None):
    if not books_list:
        books_list = books
    
    print("Book List:")
    for book in books_list:
        print("Title:", book['title'])
        print("Author:", book['author'])
        print("Genre:", book['genre'])
        print("ISBN:", book['isbn'])
        print("")

# Stage 3: User Interface

def display_menu():
    print("==== Library Management System ====")
    print("1. Add a book")
    print("2. Update a book")
    print("3. Delete a book")
    print("4. Search for books")
    print("5. Display all book1s")
    print("8. Borrow a book")
    print("9. Return a book")
    print("6. Exit")

def handle_user_input():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '5':
            display_books()
        elif choice == '8':
            borrow_book()
        elif choice == '9':
            return_book()
        elif choice == '6':
            save_books_to_file()
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")
        

# Stage 4: File Handling

def save_books_to_file():
    with open(filename, 'w') as file:
        json.dump(books, file)
    print("Books saved to file successfully.")

def load_books_from_file():
    global books
    try:
        with open(filename, 'r') as file:
            books = json.load(file)
        print("Books loaded from file successfully.")
    except FileNotFoundError:
        print("No existing file found. Starting with an empty book list.")

# Stage 5: Additional Functionality
    # Implement book borrowing functionality 
def borrow_book():
    title = input("Enter the book title to borrow: ")

    for book in books:
        if book['title'] == title:
            if book.get('borrower'):
                print("Sorry, the book is already borrowed.")
            else:
                borrower_name = input("Enter the borrower's name: ")
                book['borrower'] = borrower_name
                print("Book borrowed successfully!")
            return

    print("Book not found!")
    
    
  # Implement book returning functionality here
def return_book():
    title = input("Enter the book title to return: ")

    for book in books:
        if book['title'] == title:
            if book.get('borrower'):
                borrower_name = book['borrower']
                del book['borrower']
                print("Book returned successfully!")
                print("Borrower:", borrower_name)
            else:
                print("The book is not currently borrowed.")
            return

    print("Book not found!")


# Main function to start the Library Management System

def main():
    load_books_from_file()
    handle_user_input()

if __name__ == "__main__":
    main()