#!/usr/bin/python3
"""script to export data in the CSV format."""
if __name__ == '__main__':
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
    with open(f'{USER_ID}.csv', 'w') as file:
        for dictionary in tasks_response.json():
            completed_key = dictionary['completed']
            title_key = dictionary['title']
            file.write(
                f'"{USER_ID}","{USERNAME}","{completed_key}","{title_key}"\n'
            )
