#!/usr/bin/python3
"""This python script fetches the REST API for todo lists of employees,
    which is available at https://jsonplaceholder.typicode.com/users
    and saves the information to a JSON file.
    Usage:
    python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests
import sys

# This script will fetch all the user information from the JSONPlaceholder API
# and store it in a dictionary of lists of dictionaries, where the key is the
# user ID and the value is a list of dictionaries containing the task title,
# completed status, and username.
if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    # Get the information from the users API endpoint and store it in the
    # users dictionary with the user ID as the key
    resp = requests.get(url)
    Users = resp.json()

    # This for loop goes through all the users and retrieves their
    # task information and stores it in the users_dict dictionary.
    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        url = url + '/todos/'
        resp = requests.get(url)

        # Retrieves the tasks associated with a user and stores them in the
        # tasks variable
        tasks = resp.json()
        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
        # This for loop retrieves the user's task information and stores it in
        # the users_dict dictionary. The key is the user_id and the value is a
        # list of dictionaries, where each dictionary contains the task title,
        # completed status, and username.
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
