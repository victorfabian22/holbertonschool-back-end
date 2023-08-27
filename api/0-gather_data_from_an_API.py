#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == '__main__':
    # URL de la REST API
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    # ID de empleados
    empoleye = int(sys.argv[1])

    # Hacemos la solicitud GET al punto final '/todos' para obtener la lista
    # TODO para el empleado dado
    response = requests.get(f'{BASE_URL}/todos?userId={empoleye}')

    # Analizamos la respuesta JSON y contamos la cantidad de tareas completadas
    todos = response.json()
    tasks_completed = [todo for todo in todos if todo['completed']]
    num_tasks_completed = len(tasks_completed)
    num_tasks = len(todos)

    # Obtenemos el nombre del empleado del punto final '/users'
    user_response = requests.get(f'{BASE_URL}/users/{empoleye}')
    user_data = user_response.json()
    empoleye_name = user_data['name']

    # Imprimimos la información de la lista
    print(f"Employee {empoleye_name} is donde with tasks \
           ({num_tasks_completed}/{num_tasks}): ")

    for todo in tasks_completed:
        print(f'	 {todo["title"]}')
