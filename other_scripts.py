

def delete_contact_by_phone(file_name, phone):
    load_file = read_file(file_name)
    for entry in load_file:
        if entry['phone'] == phone:
            load_file.remove(entry)
    rewrite_file(file_name, load_file)

import math


def make_volume_threedimensional_shape(shape: str):
    def volume_shape(r=0.0, h=0.0):
        formula_dict = {
            'шар': 4 / 3 * math.pi * r ** 3,
            'конус': 1 / 3 * math.pi * r ** 2 * h,
            'цилиндр': math.pi * r ** 2 * h
        }
        return [formula_dict[key] for key in formula_dict if key == shape]
    return volume_shape


if __name__ == "__main__":
    print(make_volume_threedimensional_shape('конус')(1.52, 2))


# way_2
def action_for_in(iterable: list):
    if not isinstance(iterable, list):
        raise TypeError
    iterator = iter(iterable)
    iterating_finished = False
    while not iterating_finished:
        try:
            yield next(iterator)
        except StopIteration:
            iterating_finished = True
