import unittest
import phone_book_app_for_task2

phone_book = 'phone_book.json'


class PhoneBookTestCase(unittest.TestCase):

    def test_add_contact(self):
        new_entry = {
            'name': 'Mykola',
            'last_name': 'Mykolenko',
            'phone': '74757575',
            'country': 'Ukraine',
            'city': 'Kyiv'
        }
        phone_book_app_for_task2.add_contact(phone_book, new_entry)
        self.assertIn(new_entry, phone_book_app_for_task2.read_file(phone_book))

    def test_delete_contact(self):
        pass

    def test_change_contact(self):
        pass

    def test_search_contact(self):
        pass


if __name__ == "__main__":
    unittest.main()
