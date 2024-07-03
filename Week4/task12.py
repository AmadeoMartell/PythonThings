import json

def convert_and_print(dictionary):
    json_data = json.dumps(dictionary)

    print(json_data)

example_dict = {'name': 'John',
    'age': 30,
    'city': 'New York',
    'email': 'john@example.com'}

convert_and_print(example_dict)
