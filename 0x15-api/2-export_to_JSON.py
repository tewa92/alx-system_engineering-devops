#!/usr/bin/python3
"""
This script will retrieve user information and their completed tasks
from the JSONPlaceholder API and export them to a JSON file
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    res = requests.get(url_to_user)
    """
    Retrieves user information from the JSONPlaceholder API
    and saves it to a JSON file
    """
    USERNAME = res.json().get('username')
    """
    Retrieves user information from the JSONPlaceholder API
    and saves it to a JSON file
    """
    url_to_task = url_to_user + '/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    # Create an empty dictionary to store the user information and their
    # completed tasks
    # The key will be the user_id and the value will be a list of
    # dictionaries containing the task title,
    # completed status, and username
    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
    # print(dict_data)
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict_data, f)
