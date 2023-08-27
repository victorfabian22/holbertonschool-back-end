#!/usr/bin/python3
"""Export to CSV"""
import csv
import json
import requests
from sys import argv


def main():
    # URL de la REST API
    BASE_URL = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    BASE_TODOS = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"

    user = requests.get(BASE_URL)
    todo = requests.get(BASE_TODOS)
    lis = []

    # Obtenemos cada valor con 'get'
    for t in todo.json():
        line = [f"{user.json().get('id')}",
                f"{user.json().get('username')}",
                f"{t.get('completed')}",
                f"{t.get('title')}"]
        lis.append(line)

    with open(f"{argv[1]}.csv", 'w') as file:
        wite = csv.writer(file, quoting=csv.QUOTE_ALL)
        wite.writerows(lis)


if __name__ == '__main__':
    main()
