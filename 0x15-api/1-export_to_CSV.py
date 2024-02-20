#!/usr/bin/python3
"""script to export data in the CSV format."""
if __name__ == '__main__':
    from csv import writer
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
        file_writer = writer(file)

        for dictionary in tasks_response.json():
            file_data = [
                str(USER_ID), str(USERNAME), str(dictionary['completed']),
                str(dictionary['title'])
            ]
            file_writer.writerow(file_data)
