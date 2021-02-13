import json


# получение листа с координатами из файла
def get_coord_list(file_name):
    with open(file_name) as f:
        file_content = json.load(f)
    coord_list = file_content['features'][0]['geometry']['coordinates']
    return coord_list


# перестановка координат в списке
def reverse_coordinates(coord_list):
    for element in coord_list:
        if type(element[0]) == list:
            reverse_coordinates(element)
        else:
            element[0], element[1] = element[1], element[0]
    return coord_list


# запись нового списка с координатами в файл
def write_coord_list_to_file(file_name, coord_list):
    with open(file_name) as f:
        file_content = json.load(f)
    file_content['features'][0]['geometry']['coordinates'] = coord_list
    with open(file_name, 'w') as f:
        json.dump(file_content, f)


def reverse_coordinates_in_file(file_name):
    write_coord_list_to_file(file_name, reverse_coordinates(get_coord_list(file_name)))


if __name__ == "__main__":
    reverse_coordinates_in_file('ato.json')
