#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list progress """
import requests
import json
import sys


if __name__ == "__main__":
    """ starts """
    user = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                        .format(sys.argv[1]))
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))
    user_data = user.json()
    tasks_data = tasks.json()
    total_tasks = 0
    done_tasks = 0
    for tasks in tasks_data:
        if tasks['completed'] is True:
            done_tasks = done_tasks + 1
        total_tasks = total_tasks + 1
    print("Employee {} is done with tasks({}/{}):".
          format(user_data[0]['name'], done_tasks, total_tasks))
    for tasks in tasks_data:
        if tasks['completed'] is True:
            print("\t {}".format(tasks['title']))
