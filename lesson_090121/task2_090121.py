import json


def read_file(file_name):
    with open(file_name) as file_object:
        load_file = json.load(file_object)
        return load_file


def rewrite_file(file_name, new_content):
    with open(file_name, 'w') as file_object:
        json.dump(new_content, file_object)


def print_contact(contact):
    print('_' * 30)
    for k, v in contact.items():
        print('|', k, ':', v)


def print_contact_list(contact_list):
    for contact in contact_list:
        print_contact(contact)


def print_file(file_name):
    load_file = read_file(file_name)
    for entry in load_file:
        print_contact(entry)


def input_contact():
    new_contact = {
        'name': input('Input name: '),
        'last_name': input('Input last name: '),
        'phone': input('Input phone: '),
        'country': input('Input country: '),
        'city': input('Input city: ')
    }
    return new_contact


def add_contact(file_name, new_contact):
    load_file = read_file(file_name)
    load_file.append(new_contact)
    rewrite_file(file_name, load_file)


def input_search_parameter():
    search_parameter = (input('Поиск контакта по имени (n), фамилии (l), телефону (p), стране(co), городу (ci).\n'
                              'Введите параметр поиска: ')).lower()
    return search_parameter


def input_search_value():
    search_value = (input('Введите значение: ')).lower()
    return search_value


def dict_parameters():
    parameters = {
        'n': 'name',
        'l': 'last_name',
        'p': 'phone',
        'co': 'country',
        'ci': 'city'
    }
    return parameters


def make_search_contact_list(file_name, search_parameter, search_value):
    parameters = dict_parameters()
    load_file = read_file(file_name)
    search_contact_list = []
    for parameter in parameters.keys():
        if parameter == search_parameter:
            for contact in load_file:
                if contact[parameters[parameter]] == search_value:
                    search_contact_list.append(contact)
    return search_contact_list


def delete_contacts(file_name, deleted_contact_list):
    load_file = read_file(file_name)
    for contact in deleted_contact_list:
        load_file.remove(contact)
    rewrite_file(file_name, load_file)


def change_contacts(change_contact_list):
    for contact in change_contact_list:
        new_contact = input_contact()
        for k in new_contact.keys():
            if new_contact[k]:
                contact[k] = new_contact[k]
    return change_contact_list


if __name__ == "__main__":
    phone_book = 'phone_book.json'
    action = input('Выберите действие для работы с телефонной книгой:\n'
                   '1. Показать всю телефонную книгу\n2. Добавить новый контакт\n'
                   '3. Найти контакт\n4. Удалить контакт по номеру телефона \n'
                   '5. Обновить контакт по номеру телефона\n6. Выйти из программы\n')
    if action == '1':
        print_file(phone_book)
    elif action == '2':
        add_contact(phone_book, input_contact())
    elif action == '3':
        found_contacts = make_search_contact_list(phone_book, input_search_parameter(), input_search_value())
        print_contact_list(found_contacts)
    elif action == '4':
        contacts_by_phone = make_search_contact_list(phone_book, 'p', input_search_value())
        delete_contacts(phone_book, contacts_by_phone)
    elif action == '5':
        contacts_by_phone = make_search_contact_list(phone_book, 'p', input_search_value())
        print_contact_list(contacts_by_phone)
        delete_contacts(phone_book, contacts_by_phone)
        for contact in change_contacts(contacts_by_phone):
            add_contact(phone_book, contact)
    else:
        print('Exit')