#!/usr/bin/python3
"""Returns information about an employee's progress
in their TODO list by providing the employee ID"""
from requests import get
from sys import argv

if __name__ == "__main__":
    """ Obtaining TODO list data from the API"""
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    # Initializing variables
    completed = 0
    total = 0
    tasks = []

    # Fetching user data from the API
    response2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = response2.json()

    # Finding the employee's name based on the provided employee ID
    for user in data2:
        if user.get('id') == int(argv[1]):
            employee = user.get('name')

    # Calculating the number of completed tasks and total tasks
    for todo in data:
        if todo.get('userId') == int(argv[1]):
            total += 1
            if todo.get('completed'):
                completed += 1
                tasks.append(todo.get('title'))

    # Printing the employee's progress information
    print("Employee {} has completed tasks: {}/{}:".format(
        employee, completed, total))
    for task in tasks:
        print("\t {}".format(task))
