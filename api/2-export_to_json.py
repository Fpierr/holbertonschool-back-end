#!/usr/bin/python3
"""extend Python script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    # Check if the employee ID is passed as an argument
    if len(sys.argv) != 2:
        print(f"missing employee id as argument")
        sys.exit(1)

    # API URL
    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    # Retrieve employee's tasks from the API
    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    # Get the username of the employee
    username = data[0]["user"]["username"]

    # Create a dictionary to store user tasks
    USER_TASK = {EMPLOYEE_ID: []}

    # Iterate through tasks and add them to the dictionary
    for task in data:
        dic_task = {"task": task["title"], "completed": task["completed"],
                    "username": username}
        USER_TASK[EMPLOYEE_ID].append(dic_task)

    # Define the filename for the JSON file
    fileName = f"{EMPLOYEE_ID}.json"

    # Write the data to the JSON file
    with open(fileName, "w") as file:
        json.dump(USER_TASK, file)
