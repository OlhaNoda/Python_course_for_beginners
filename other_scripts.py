

def delete_contact_by_phone(file_name, phone):
    load_file = read_file(file_name)
    for entry in load_file:
        if entry['phone'] == phone:
            load_file.remove(entry)
    rewrite_file(file_name, load_file)