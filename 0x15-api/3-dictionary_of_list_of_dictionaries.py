#!/usr/bin/python3
""" Python script to export data in the CSV format """
import json
import requests
import sys


if __name__ == "__main__":
        user = requests.get('https://jsonplaceholder.typicode.com/users')
        user_data = user.json()
        lista = []
        dic = {}
        for user in user_data:
                u = user['id']
                text = 'https://jsonplaceholder.typicode.com/todos?userId={}?'
                .format(u)
                t = requests.get(text)
                tasks_data = t.json()
                for tasks in tasks_data:
                        t = '{}'.format(tasks.get('title'))
                        username = '{}'.format(user_data[u - 1]['username'])
                        di = {'task': t, 'completed': tasks.get('completed'),
                              'username': username}
                        lista.append(di)
                dic.update({u: lista})
        with open('todo_all_employees.json', 'w+', encoding='utf-8') as f:
                json.dump(dic, f)
