from lib.todo_search import * 
import pytest 


# Empty string returns "No text provided"
def test_empty_string():
    with pytest.raises(Exception) as e:
        includes_todo()
        error_message = str(e.value)
        assert error_message == "No text provided"

