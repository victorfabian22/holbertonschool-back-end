#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    todo = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    us = requests.get(user)
    to = requests.get(todo)
    tr = []
    for dicc in to.json():
        for k, v in dicc.items():
            if k == 'completed':
                if v is True:
                    tr.append(dicc)
    print(f"Employee {us.json().get('name')} is \
done with tasks({(len(tr))}/{(len(to.json()))}):")
    for tittle in tr:
        for k, v in tittle.items():
            if k == 'title':
                print(f'	 {v}')
