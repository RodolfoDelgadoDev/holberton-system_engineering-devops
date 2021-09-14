#!/usr/bin/python3
""" Python script to export data in the CSV format """
import json
import requests
import sys


if __name__ == "__main__":
        user = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.
                            format(sys.argv[1]))
        u = "{}".format(sys.argv[1])
        text = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(u)
        t = requests.get(text)
        user_data = user.json()
        tasks_data = t.json()
        filename = '{}.json'.format(u)
        lista = []
        for tasks in tasks_data:
                task = '{}'.format(tasks['title'])
                username = '{}'.format(user_data[0]['username'])
                di = {'task': task, 'completed': tasks['completed'],
                      'username': username}
                lista.append(di)
        dic = {u: lista}
        with open(filename, 'w+', encoding='utf-8') as f:
                json.dump(dic, f)
