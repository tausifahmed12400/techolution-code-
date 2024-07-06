import json

class CheckoutManager:
    def __init__(self):
        self.checkouts = []

    def user_exists(self, user_id, user_manager):
        users = user_manager.users
        for user in users:
            if user.user_id == user_id:  # Access user_id directly from User object
                return True
        return False

    def checkout_book(self, user_id, isbn, book_manager, user_manager):
        if not self.user_exists(user_id, user_manager):
            print(f"User with ID {user_id} does not exist. Cannot check out the book.")
            return False

        # Check if the book is available
        book = book_manager.search_books(isbn=isbn)
        if not book or not book[0].available:
            print(f"Book with ISBN {isbn} is not available for checkout.")
            return False

        if book_manager.update_book_availability(isbn, False):
            self.checkouts.append({"user_id": user_id, "isbn": isbn})
            self.save_checkouts()
            return True
        else:
            print(f"Book with ISBN {isbn} is not available for checkout.")
            return False

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}")

    def save_checkouts(self):
        # Implement save functionality if required (e.g., saving to a file)
        pass
