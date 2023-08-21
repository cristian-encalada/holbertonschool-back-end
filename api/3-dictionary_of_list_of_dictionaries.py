#!/usr/bin/python3
""" [3] Dictionary of list of dictionaries
Python script to export data in the JSON format
"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Obtain the list of all users
    users_endpoint = f"{base_url}/users/"
    users_data = get(users_endpoint).json()

    all_users = {}

    for user in users_data:
        user_id = user["id"]
        user_name = user["username"]
        # Endpoint URLs for user and todos data
        todos_endpoint = f"{base_url}/todos/?userId={user_id}"
        todos_data = get(todos_endpoint).json()

        # Store data for one user in JSON format
        user_data = [
            {
                "username": user_name,
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos_data
        ]
        all_users[user_id] = user_data

    # Create a JSON file for writing
    filename = f"todo_all_employees.json"
    with open(filename, mode="w") as json_file:
        dump(all_users, json_file)
