
def one_stih(file_name=''):
    with open(file_name) as f:
        for line in f:
            yield line


def stihi(*args):
    all_iterators = []
    for fn in args:
        all_iterators.append(one_stih(fn))
    ok = True
    while ok:
        ok = False
        for one in all_iterators:
            try:
                ret = next(one)
                ok = True
                yield ret
            except:
                pass


if __name__ == "__main__":
    for line in stihi('1.txt', '2.txt'):
        print(line)
