def find_by_id(items, item_id):

    for item in items:

        if item.id == item_id:
            return item
        
    return None


def find_by_name(items, item_name):

    for item in items:

        if item.name.lower() == item_name.lower():
            return item
        
    return None


def get_text_input(message, error_message="invalid input!"):

    while True:

        value = input(message).strip()

        if value:
            return value
        
        print(error_message)


def get_int_input(message, error_message="invalid input!"):

    while True:
        value = input(message).strip()

        if value.isdigit():
            return int(value)
        
        print(error_message)
    

def get_search_input(message):

    return input(message).strip()


def get_choice(message):

    valid_choices = [str(i) for i in range(1, 16)]

    while True:

        value = input(message).strip()

        if value in valid_choices:
            return value
    
        print("invalid choice!")


def find_item(items, keyword):

    if keyword.isdigit():
        return find_by_id(items, int(keyword))
    
    return find_by_name(items, keyword)
