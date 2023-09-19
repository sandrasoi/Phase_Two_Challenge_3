from lib.todo_search import * 
import pytest 


# Empty string returns "No text provided"
def test_empty_string():
    with pytest.raises(Exception) as e:
        includes_todo()
        error_message = str(e.value)
        assert error_message == "No text provided"

#Text containing #TODO returns "Yes"
string = 'Example text #TODO'
def test_todo_in_text():
    result = includes_todo(string)
    assert result == "Yes"

#Text containing #Todo in lowecase returns "No"
def test_todo_lower_in_text():
    result = includes_todo("Example text #Todo")
    assert result == "No"

#Text not containing #TODO returns "No"
def test_todo_not_in_text():
    result = includes_todo("Example text.")
    assert result == "No"



