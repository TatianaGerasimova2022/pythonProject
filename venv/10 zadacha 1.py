import requests

def endpoint_descriptions():
    url = 'http://api.dataatwork.org/v1/jobs'
    response = requests.get(url).json()
    print(response)
endpoint_descriptions()

