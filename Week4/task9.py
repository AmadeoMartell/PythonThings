import json

typo_json = '{"name": "<NAME>", "age": 20, "city": "New York"}'

obj = json.loads(typo_json)

for key, value in obj.items():
    print(f'{key}: {value}')