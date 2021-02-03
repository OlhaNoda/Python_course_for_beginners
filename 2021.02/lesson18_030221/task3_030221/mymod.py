def count_lines(file_name):
    return len(open(file_name).readlines())


def count_chars(file_name):
    return len(open(file_name).read())


def test(file_name):
    count_lines(file_name)
    count_chars(file_name)
