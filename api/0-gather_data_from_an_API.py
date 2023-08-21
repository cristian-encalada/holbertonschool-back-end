#!/usr/bin/python3
""" [0] Gather data from an API
Using jsonplaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
from requests import get
from sys import argv

if __name__ == "__main__":

    # Get the user ID from command line argument
    user_id = argv[1]

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    # Endpoint URLs for user and todos data
    user_endpoint = f"{base_url}/users/{user_id}"
    todos_endpoint = f"{base_url}/todos/?userId={user_id}"

    # Get user data and extract the name
    user_data = get(user_endpoint).json()
    user_name = user_data.get("name")
    # Get todos data and find completed tasks
    todos_data = get(todos_endpoint).json()
    completed_tasks = []
    for task in todos_data:
        if task["completed"]:
            completed_tasks.append(task["title"])

    total_tasks = len(todos_data)
    num_completed_tasks = len(completed_tasks)

    # Print employee's TODO progress and completed tasks
    print(f"Employee {user_name} is done with tasks"
          f"({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")
