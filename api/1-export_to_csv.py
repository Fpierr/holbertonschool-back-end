#!/usr/bin/python3
"""Exports employee's TODO list progress to a CSV file"""

import csv
import requests
import sys


if __name__ == "__main__":
    """Check if the employee ID is passed as an argument"""
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

    # Get employee name from the received data
    EMPLOYEE_NAME = data[0]["user"]["username"]
    fileName = f"{EMPLOYEE_ID}.csv"

    # Write data to the CSV file
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        # Iterate through employee's tasks and write to the CSV file
        for task in data:
            writer.writerow(
                [EMPLOYEE_ID, EMPLOYEE_NAME, str(task["completed"]),
                 task["title"]]
            )
