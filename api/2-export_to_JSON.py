#!/usr/bin/python3
""" [2] Export to JSON
Python script to export data in the JSON format
"""
from json import dump
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

    # Get user data and extract the username
    user_data = get(user_endpoint).json()
    user_name = user_data.get("username")
    # Get todos data list
    todos_data = get(todos_endpoint).json()

    # Format the JSON data
    json_data = {
        str(user_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name
            }
            for task in todos_data
        ]
    }

    # Create a JSON file for writing
    filename = f"{user_id}.json"
    with open(filename, mode="w") as json_file:
        dump(json_data, json_file)
