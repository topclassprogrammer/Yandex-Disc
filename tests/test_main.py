from main import create_folder, check_if_folder_exists


def test_create_folder():
    expected = 201
    assert create_folder() == expected


def test_check_if_folder_exists():
    expected = True
    assert check_if_folder_exists() == expected
