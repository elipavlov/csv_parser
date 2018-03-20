from os import path

from csv_parser.storage import Storage


csv_pth = path.join(path.dirname(__file__), 'test_storage.csv')


def test_storage_find_entry_without_aliases():
    storage = Storage(csv_pth)

    food, aliases = storage.find_entry('Лепешка ржаная')

    assert food
    assert food.name == 'лепешка ржаная'
    assert len(aliases) == 0


def test_storage_find_entry_with_aliases():
    storage = Storage(csv_pth)

    food, aliases = storage.find_entry('Лепешка ржаная', True)

    assert food
    assert food.name == 'лепешка ржаная'
    assert len(aliases) == 1

