import json

typo_json = {"name": "<NAME>", "age": None, "city": "New York"}

obj = json.dumps(typo_json)

print(obj)