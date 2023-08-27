#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(BASE_URL)
    dic = {}

    for i in users.json():
        url = f"https://jsonplaceholder.typicode.com/users/{i.get('id')}/todos"
        todo = requests.get(url)
        lis = []

        for q in todo.json():
            new = {'username': f"{i.get('username')}",
                   'task': f"{q.get('title')}",
                   'completed': q.get('completed')}
            lis.append(new)
        dic[f"{i.get('id')}"] = lis

    with open("todo_all_employees.json", 'w') as file:
        json.dump(dic, file)
