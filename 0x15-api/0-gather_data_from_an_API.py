#!/usr/bin/python3
# This is the main entry point for this script
# It can be run from the command line by specifying an employee id
# e.g. python3 0-gather_data_from_an_API.py 1
# This script will output information about the employee and their
# completed tasks
# This script uses the JSONPlaceholder API to get information about an
# employee and their completed tasks

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    # Check if the employee ID is provided as a command-line argument
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            # Retrieve the user's information
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            # Retrieve the user's completed tasks
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            # Filter the completed tasks
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
