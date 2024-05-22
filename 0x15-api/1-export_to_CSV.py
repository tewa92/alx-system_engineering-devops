#!/usr/bin/python3
"""
This script exports user information and their completed tasks to a CSV file
from the JSONPlaceholder API

Usage:
    python3 1-export_to_CSV.py <user_id>
"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    # Get user information
    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            # True if the task is completed, False otherwise
            title_task = task.get('title')
            # The task is completed if completed is True, otherwise False
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
