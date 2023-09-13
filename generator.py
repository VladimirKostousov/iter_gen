import types


def flat_generator(list_of_lists):
    gen = (list_of_lists[i][j] for i in range(0, len(list_of_lists)) for j in range(0, len(list_of_lists[i])))
    return gen


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    print(list(flat_generator(list_of_lists_1)))


if __name__ == '__main__':
    test_2()
