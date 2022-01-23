#import os
import forex_python
import json
#import boto3
import requests

url = 'https://api.exchangerate.host/convert?from=USD&to=EUR'
response = requests.get(url)
data = response.json()

print(data)