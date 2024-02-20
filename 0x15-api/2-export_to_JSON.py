#!/usr/bin/python3
"""script to export data in the JSON format."""
if __name__ == '__main__':
    import json
    import requests
    import sys

    USER_ID = sys.argv[1]

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    )
    USERNAME = response.json()['username']
    tasks_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos/?userId={USER_ID}'
    )
    with open(f'{USER_ID}.json', 'w') as file:
        for dictionary in tasks_response.json():
            completed_key = dictionary['completed']
            title_key = dictionary['title']
            json_string = {
                f"{USER_ID}": [
                    {
                        "task": dictionary['title'],
                        "completed": dictionary['completed'],
                        "username": USERNAME
                    }
                ]
            }
            file.write(json.dumps(json_string))
