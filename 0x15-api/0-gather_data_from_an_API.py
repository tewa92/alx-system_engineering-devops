#!/usr/bin/python3
# This is the main entry point for this script
# It can be run from the command line by specifying an employee id
# e.g. python3 0-gather_data_from_an_API.py 1
# This script will output information about the employee and their
# completed tasks
# This script uses the JSONPlaceholder API to get information about an
# employee and their completed tasks
import requests
import sys
# The user ID must be passed as a command line argument
REST_API = "https://jsonplaceholder.typicode.com/"
# This API is just a placeholder and doesn't actually contain any data
# It's used in this script to demonstrate how to make a GET request
# to a REST API to fetch data about an employee and their completed tasks
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)
    # Check for correct usage of command line argument
    employee_id = sys.argv[1]
    user = requests.get(REST_API + "users/{}".format(employee_id)).json()
    todos = requests.get(REST_API + "todos?userId={}".format(employee_id))
    .json()
    # This is the part of the script that makes the GET request
    # to the API to fetch the data about the user and their todos
    completed_tasks = [task for task in todos if task.get("completed") is True]
    # This is the list of all the completed tasks for the given user
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    # Print the list of completed tasks for the given user
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
