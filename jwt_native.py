# Create and authenticate a Cisco Webex Teams JWT using native Python
#
# Script Dependencies:
#     requests
#
# Depencency Installation:
#     $ pip install requests
#
# Copyright (c) 2018 Cisco and/or its affiliates.
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 

import hashlib
import hmac
import base64
import requests
import time
import json
import math

secrets = json.load(open('secrets.json', 'r')) # Put guest issuer id/secret in secrets.json

header = {
            "alg": "HS256",
            "typ":"JWT"
         }

expiration =  math.floor(time.time()) + 3600 # 1 hour from now


# 'sub'/subject will be use to create the Webex Teams user email (sub@org-uuid)
# 'name' will be the user's display name 
payload = {
            "sub": "testSubject1",
            "name": "testName1",
            "iss": secrets['WEBEX_TEAMS_ISSUER_ID'],
            "exp": expiration
          }

header_byt = bytearray(json.dumps(header),'utf-8')
header_b64 = base64.b64encode(header_byt)
header_str = header_b64.decode('utf-8').replace('=','')

payload_byt = bytearray(json.dumps(payload),'utf-8')
payload_b64 = base64.b64encode(payload_byt)
payload_str = payload_b64.decode('utf-8').replace('=','')

content = header_str+"."+payload_str

secret = base64.b64decode(secrets['WEBEX_TEAMS_ISSUER_SECRET'])

hash = hmac.new(secret, content.encode('utf-8'), digestmod=hashlib.sha256).digest()
signature = base64.b64encode(hash).decode('utf-8')

jwtToken = header_str+'.'+payload_str+'.'+signature
print(jwtToken)

headers = { 'Authorization': 'Bearer ' + jwtToken }

try:
    resp = requests.post(url="https://api.ciscospark.com/v1/jwt/login", headers = headers )
    print(resp.text)
except requests.exceptions.RequestException as error:
    print(error)
