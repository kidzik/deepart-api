import tempfile
import json
import requests
import sys
from settings import *

def main():
    """
    Ensure we can create a new account object.
    """
    if len(sys.argv) == 1:
        print("You need to specify the order ID")
        return
    
    host = "https://deepart.io"
    url = '/api/token-auth/'
    data = {"username": DEEPART_LOGIN, "password": DEEPART_PASSWORD}
    response = requests.post(host + url, data = data)

    print(response.text)
    resp = json.loads(response.text)
    token = resp["token"]
    headers={'Authorization': "Token %s" % token}

    response = requests.get(host + '/api/myorders/%s/' % sys.argv[1], {}, headers = headers)
    print(response.text)
        
main()
