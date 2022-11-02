from ipapi import get_location

def get_length():
    return len(get_location())

def test_length():
    assert get_length == 9