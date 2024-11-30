import pytest
from count_sentences import MyString

def test_value_string():
    '''raises ValueError if value is not a string.'''
    with pytest.raises(ValueError) as excinfo:
        string = MyString(123)  # passing a non-string value
    assert str(excinfo.value) == "The value must be a string."

def test_is_sentence():
    '''Test if the string ends with a period.'''
    string = MyString("This is a sentence.")
    assert string.is_sentence() is True
    string = MyString("This is not a sentence")
    assert string.is_sentence() is False

def test_is_question():
    '''Test if the string ends with a question mark.'''
    string = MyString("Is this a question?")
    assert string.is_question() is True
    string = MyString("This is not a question")
    assert string.is_question() is False

def test_is_exclamation():
    '''Test if the string ends with an exclamation mark.'''
    string = MyString("Wow, amazing!")
    assert string.is_exclamation() is True
    string = MyString("This is not an exclamation")
    assert string.is_exclamation() is False

def test_count_sentences():
    '''Test to count the number of sentences in the string.'''
    string = MyString("This is a sentence! This is another sentence. Is this a question?")
    assert string.count_sentences() == 3  # Three sentences

    string = MyString("This is one sentence.")
    assert string.count_sentences() == 1  # One sentence

    string = MyString("No punctuation")
    assert string.count_sentences() == 1  # Only one sentence, no punctuation at the end

    string = MyString("!!")
    assert string.count_sentences() == 0  # No sentences

