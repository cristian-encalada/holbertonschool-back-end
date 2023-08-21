#!/usr/bin/python3
""" [1] Export to CSV
Python script to export data in the CSV format
"""
from csv import writer, QUOTE_ALL
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
    # Create a CSV file for writing
    filename = f"{user_id}.csv"
    with open(filename, mode="w") as csv_file:
        csv_writer = writer(csv_file, quoting=QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([
                user_id,
                user_name,
                task["completed"],
                task["title"]
            ])
