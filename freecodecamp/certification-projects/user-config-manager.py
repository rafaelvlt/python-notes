def add_setting(dict_settings, tuple_settings):
    new_key = tuple_settings[0].lower()
    new_value = tuple_settings[1].lower()

    if new_key in dict_settings:
        return f"Setting '{new_key}' already exists! Cannot add a new setting with this name."
    else:
        dict_settings[new_key] = new_value
        return f"Setting '{new_key}' added with value '{new_value}' successfully!"

def update_setting(dict_settings, tuple_settings):
    new_key = tuple_settings[0].lower()
    new_value = tuple_settings[1].lower()

    if new_key in dict_settings:
        dict_settings[new_key] = new_value
        return f"Setting '{new_key}' updated to '{new_value}' successfully!"
    else:
        return f"Setting '{new_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_settings, key):
    key = key.lower()

    if key in dict_settings:
        dict_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dict_settings):
    if not dict_settings:
        return "No settings available."

    final_str = "Current User Settings:\n"
    for key, value in dict_settings.items():
        final_str += key.capitalize() + ': ' + value + '\n' 

    return final_str

test_settings = {'theme': 'dark', 'volume': 'high'}
