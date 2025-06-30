import pytest
from validate_filenames import validate_filename
from fix_filenames      import fix_filename

@pytest.mark.parametrize("filename,expected", [
    ("BA4592-311_front_1.jpg", True),
    ("BA2037-089_back_2.JPG",   True),
    ("BA4592-311_front_1",      False),
    ("XX0000-000_front_1.jpg",  False),
    ("BA4592-311__front_1.jpg", True),
    ("BA4592-311_frönt_1.jpg",  False),
])
def test_validate_filename(filename, expected):
    assert validate_filename(filename) == expected

@pytest.mark.parametrize("input_filename,expected", [
    ("BA4592-311_Front_1.JPG",  "ba4592-311_front_1.jpg"),
    ("BA4592 311 front 1.jpg",  "ba4592-311_front_1.jpg"),
    ("BA4592-311_front_1.JpG",  "ba4592-311_front_1.jpg"),
    ("bad_name.jpg",            None),
])
def test_fix_filename(input_filename, expected):
    assert fix_filename(input_filename) == expected
