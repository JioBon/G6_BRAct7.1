from ipapi import get_location

def get_length(): # Getting the Length of the Api
    return len(get_location())

def test_length(): # Testing the length on api
    assert get_length() == 9

def test_null(): # Check if values are not null
    for i in get_location():
        assert i != None