#!/usr/bin/python3
""" Python script to export data in the CSV format """
import csv
import json
import requests
import sys


if __name__ == "__main__":
        user = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                            .format(sys.argv[1]))
        t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(sys.argv[1]))
        user_data = user.json()
        tasks_data = t.json()

        filename = '{}.csv'.format(sys.argv[1])
        with open(filename, 'w+', encoding='utf-8') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for tasks in tasks_data:
                    lista = []
                    a = '{}'.format(tasks['userId'])
                    b = '{}'.format(user_data[0]['username'])
                    c = '{}'.format(tasks['completed'])
                    d = '{}'.format(tasks['title'])
                    lista.append(a)
                    lista.append(b)
                    lista.append(c)
                    lista.append(d)
                    writer.writerow(lista)
