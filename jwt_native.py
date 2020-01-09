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
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
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
import os

# Load secrets from .env file into environment, if not already existing
from dotenv import load_dotenv
load_dotenv()

# Create a JWT header object - HMAC SHA256/JWT are always used
header = {
            'alg': 'HS256',
            'typ':'JWT'
         }

expiration =  math.floor(time.time()) + 3600 # 1 hour from now

# Create a JWT payload object
# 'sub' (subject) will be use to create the Webex Teams user email (sub@org-uuid)
# 'name' will be the user's display name 
payload = {
            'sub': 'testSubject1',
            'name': 'testName1',
            'iss': os.getenv('WEBEX_TEAMS_ISSUER_ID'),
            'exp': expiration
          }

# Base64 encode the header
header_byt = bytearray(json.dumps(header),'utf-8')
header_b64 = base64.b64encode(header_byt)
header_str = header_b64.decode('utf-8').replace('=','') # remove base64 padding

# Base64 encode the payload
payload_byt = bytearray(json.dumps(payload),'utf-8')
payload_b64 = base64.b64encode(payload_byt)
payload_str = payload_b64.decode('utf-8').replace('=','')

content = header_str+'.'+payload_str

# Base64 decode the Guest Issuer secret
secret = base64.b64decode(os.getenv('WEBEX_TEAMS_ISSUER_SECRET'))

# Instantiate a HMAC crypto hash using the decoded Guest Issuer shared secret
hash = hmac.new(secret, content.encode('utf-8'), digestmod = hashlib.sha256).digest()

# Create a signature by Base64 encoded the hash and convert into a string
signature = base64.b64encode(hash).decode('utf-8')

# Append the signature to the content with '.'
jwtToken = header_str+'.'+payload_str+'.'+signature

print(jwtToken)

# Exchange the signed JWT for an access token using requests
try:
    resp = requests.post(
        url = 'https://api.ciscospark.com/v1/jwt/login',
        headers = { 'Authorization': 'Bearer ' + jwtToken }
    )
    print(resp.text)
except requests.exceptions.RequestException as error:
    print(error)
