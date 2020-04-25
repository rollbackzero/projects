#!/usr/bin/env python

import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":

    auth = ('admin', 'cisco')
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    url = "https://172.16.21.254/api/interfaces/physical/GigabitEthernet0_API_SLASH_0"
    
    payload = {
        "kind": "object#GigabitInterface",
        "interfaceDesc": "Configured via Python"
    }
 
    response = requests.patch(url, data=json.dumps(payload), auth=auth, headers=headers, verify=False)
