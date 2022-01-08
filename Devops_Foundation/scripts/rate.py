import os
import forex_python
import json
import boto3

from datetime import datetime
moment=datetime.today().strftime('%Y_%m_%d_%H_%M_%S')


from forex_python.converter import CurrencyRates 
c = CurrencyRates()
rate=(c.get_rates('USD')) 
#data = rate.json()
filename='home/ec2-user/project2/data/rate_'+moment+'.json'
print(f"Executed the exchange rate code and will save the created file with a timestamp as exchangerate_{moment}")

s3_client = boto3.client('s3')
with open(filename, 'w') as json_file:
    json.dump(rate, json_file)

json_file.close()
with open(filename, 'rb') as final:
    s3_client.upload_fileobj(final, 'cloudreality', f'exchangerate_{moment}.json')
print("Successfully executed, no error and file exported as JSON")

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
sns_client = boto3.client('sns')
sns_client.publish(
    TargetArn='arn:aws:sns:us-east-1:022357963194:ExchangeRate',
    Message=f'Hello Team, \n The exchange rate for the hour file named exchangerate_{moment} have been successfully logged into CloudReality S3 bucket. The next exchange rate notification is in an hour, if none is received kindly take that as an indication of an error and act promptly. \n Thank you. \n Cloud Developer Carew Ayodeji'
)
#elif:
#print("Error occurred and job not executed")

#s3.meta.client.upload_file('filename', 'cloudreality', 'filename')


#json_dump = json. dumps(data_set)
#print(json_dump) String of JSON object.
#json_object = json. loads(json_dump)