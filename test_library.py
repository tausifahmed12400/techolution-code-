import unittest
from book import Book, BookManager
from user import User, UserManager
from check import CheckoutManager
import os
import json

class TestBookManager(unittest.TestCase):

    def setUp(self):
        # Setup a temporary storage file for testing
        self.test_file = 'test_books.json'
        self.book_manager = BookManager(storage_file=self.test_file)

    def tearDown(self):
        # Remove the test storage file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        self.book_manager.add_book('Test Title', 'Test Author', '12345')
        self.assertEqual(len(self.book_manager.books), 1)
        self.assertEqual(self.book_manager.books[0].title, 'Test Title')

    def test_list_books(self):
        self.book_manager.add_book('Test Title', 'Test Author', '12345')
        books = self.book_manager.books
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'Test Title')

    def test_search_books(self):
        self.book_manager.add_book('Test Title', 'Test Author', '12345')
        result = self.book_manager.search_books(title='Test Title')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'Test Title')

    def test_update_book_availability(self):
        self.book_manager.add_book('Test Title', 'Test Author', '12345')
        self.book_manager.update_book_availability('12345', False)
        self.assertFalse(self.book_manager.books[0].available)

class TestUserManager(unittest.TestCase):

    def setUp(self):
        # Setup a temporary storage file for testing
        self.test_file = 'test_users.json'
        self.user_manager = UserManager(storage_file=self.test_file)

    def tearDown(self):
        # Remove the test storage file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_user(self):
        self.user_manager.add_user('Test User', '1001')
        self.assertEqual(len(self.user_manager.users), 1)
        self.assertEqual(self.user_manager.users[0].name, 'Test User')

    def test_list_users(self):
        self.user_manager.add_user('Test User', '1001')
        users = self.user_manager.users
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, 'Test User')

    def test_search_users(self):
        self.user_manager.add_user('Test User', '1001')
        result = self.user_manager.search_users(name='Test User')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Test User')

class TestCheckoutManager(unittest.TestCase):

    def setUp(self):
        # Setup managers with temporary storage files for testing
        self.book_file = 'test_books.json'
        self.user_file = 'test_users.json'
        self.book_manager = BookManager(storage_file=self.book_file)
        self.user_manager = UserManager(storage_file=self.user_file)
        self.checkout_manager = CheckoutManager()

    def tearDown(self):
        # Remove the test storage files after tests
        if os.path.exists(self.book_file):
            os.remove(self.book_file)
        if os.path.exists(self.user_file):
            os.remove(self.user_file)

    def test_checkout_book(self):
        self.user_manager.add_user('Test User', '1001')
        self.book_manager.add_book('Test Title', 'Test Author', '12345')
        result = self.checkout_manager.checkout_book('1001', '12345', self.book_manager, self.user_manager)
        self.assertTrue(result)
        self.assertFalse(self.book_manager.books[0].available)

    def test_user_exists(self):
        self.user_manager.add_user('Test User', '1001')
        self.assertTrue(self.checkout_manager.user_exists('1001', self.user_manager))
        self.assertFalse(self.checkout_manager.user_exists('1002', self.user_manager))

    def test_list_checkouts(self):
        self.user_manager.add_user('Test User', '1001')
        self.book_manager.add_book('Test Title', 'Test Author', '12345')
        self.checkout_manager.checkout_book('1001', '12345', self.book_manager, self.user_manager)
        self.assertEqual(len(self.checkout_manager.checkouts), 1)
        self.assertEqual(self.checkout_manager.checkouts[0]['user_id'], '1001')

if __name__ == '__main__':
    unittest.main()
