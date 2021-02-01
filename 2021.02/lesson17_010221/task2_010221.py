import unittest
import phone_book_app_for_task2 as app

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
        app.add_contact(phone_book, new_entry)
        self.assertIn(new_entry, app.read_file(phone_book))

    def test_delete_contact(self):
        deleted_entry = app.read_file(phone_book)[0]
        app.delete_contacts(phone_book, deleted_entry)
        self.assertNotIn(deleted_entry, app.read_file(phone_book))

    def test_search_contact_by_phone(self):
        found_contacts = app.make_search_contact_list(phone_book, 'p', '123456789')
        for contact in found_contacts:
            self.assertIn(contact, app.read_file(phone_book))


if __name__ == "__main__":
    unittest.main()
