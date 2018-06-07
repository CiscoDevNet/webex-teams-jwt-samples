/* 
Create and authenticate a Cisco Webex Teams JWT using JavaScript and jsonwebtoken

Script Dependencies:
    (see package.json)

Depencency Installation:
    $ npm install

Copyright (c) 2018 Cisco and/or its affiliates.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
*/

const jwt = require('jsonwebtoken');
const request = require('request-promise-native');

const secrets = require('./secrets.json'); //Put guest issuer id/secret in secrets.json

const expiration = Math.floor(new Date() / 1000) + 3600 // 1 hour from now

// 'sub'/subject will be use to create the Webex Teams user email (sub@org-uuid)
// 'name' will be the user's display name 
const payload = {
    'sub': 'testUser1',
    'name': 'testName1',
    'iss': secrets.WEBEX_TEAMS_ISSUER_ID,
    'exp': expiration
};

const decoded = Buffer.from(secrets.WEBEX_TEAMS_ISSUER_SECRET, 'base64');

const jwtToken = jwt.sign(payload, decoded, { algorithm: 'HS256', noTimestamp: true });
console.log(jwtToken);

request.post({
    uri: 'https://api.ciscospark.com/v1/jwt/login',
    headers: { 'Authorization': 'Bearer ' + jwtToken }
})
    .then(res => { console.log(res) })
    .catch(err => { console.log(err.message) })