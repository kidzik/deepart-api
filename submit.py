import tempfile
import json
import requests
from settings import *

def main():
    """
    Ensure we can create a new account object.
    """
    host = "https://deepart.io"
    url = '/api/token-auth/'
    data = {"username": DEEPART_LOGIN, "password": DEEPART_PASSWORD}
    response = requests.post(host + url, data = data)

    resp = json.loads(response.text)
    token = resp["token"]
    headers={'Authorization': "Token %s" % token}

    response = requests.post(host + '/api/myorders/create/', {}, headers = headers)
    print(response.text)
    resp = json.loads(response.text)
    
    pk = resp['id']
    response = requests.post(host + '/api/myorders/%d/image/' % (pk,), {'whichimg': 'content', 'parent_id': '1'}, files={'image': open(DEEPART_CONTENT, 'rb')},headers = headers)


    response = requests.post(host + '/api/myorders/%d/image/' % (pk,), {'whichimg': 'style', 'parent_id': '1'}, files={'image': open(DEEPART_STYLE, 'rb')}, headers = headers)

    print("Images submitted succesfully")
        
main()
