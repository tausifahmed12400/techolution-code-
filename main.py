import book
import user
import check

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. List Checkouts")
    print("7. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = book.BookManager()
    user_manager = user.UserManager()
    checkout_manager = check.CheckoutManager()

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            if user_manager.add_user(name, user_id):
                print("User added.")
        elif choice == '4':
            user_manager.list_users()
        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            if checkout_manager.checkout_book(user_id, isbn, book_manager, user_manager):
                print("Book checked out.")
        elif choice == '6':
            checkout_manager.list_checkouts()
        elif choice == '7':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
