#!/usr/bin/python3
"""script to export data in the JSON format."""
if __name__ == '__main__':
    import json
    import requests

    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/'
    )
    with open('todo_all_employees.json', 'w') as file:
        for user in response.json():
            USER_ID = user['id']
            USERNAME = user['username']
            tasks_response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos/?userId={USER_ID}'
            )

            json_string = {
                str(USER_ID): [
                    {
                        "username": USERNAME,
                        "task": dictionary['title'],
                        "completed": dictionary['completed'],
                    }
                    for dictionary in tasks_response.json()
                ]
            }
            file.write(json.dumps(json_string))
