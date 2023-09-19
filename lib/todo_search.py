#function that returns 'Yes' if #TODO is in the text
def includes_todo(text):
    if text == "":
        raise Exception("No text provided")
    elif "#TODO" in text:
        return "Yes"
    else:
        return "No"