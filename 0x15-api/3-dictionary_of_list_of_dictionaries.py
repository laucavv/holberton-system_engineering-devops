#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    users = '{}users/'.format(url)
    request_users = requests.get(users).json()

    json_file = 'todo_all_employees.json'
    dict_user = {}
    for user in request_users:
        list_task = []
        tasks_user = requests.get('{}todos?userId={}'
                                  .format(url, user['id'])).json()
        name_user = user['username']
        for task in tasks_user:
            dics_tasks = {}
            dics_tasks['task'] = task['title']
            dics_tasks['completed'] = task['completed']
            dics_tasks['username'] = name_user
            list_task.append(dics_tasks)
        dict_user[task['userId']] = list_task
    with open(json_file, mode='w') as file:
        file_w = json.dumps(dict_user)
        file.write(file_w)
