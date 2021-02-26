import argparse
import sys
import requests
from pickle import loads, dumps


server = input()
port = input()
a = int(input())
b = int(input())

query = f"{server}:{port}?a={a}&b={b}"

response = requests.get(query)
print(*sorted(response.json()['result']))
print(response.json()['check'])

