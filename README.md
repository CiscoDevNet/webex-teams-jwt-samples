# webex-teams-jwt-samples

## Overview

Python and JavaScript sample project for [Visual Studio Code](https://code.visualstudio.com/) showing how to build and authenticate JSON Web Tokens for Cisco Webex Teams.  

Includes 'native' and popular-library examples ([PyJWT](https://pyjwt.readthedocs.io/en/latest/) / [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken))

See background information on the Webex Teams [Guest Issuer](https://developer.webex.com/docs/guest-issuer) feature

## Getting started

- Clone this repo, and navigate into the directory:

    ```shell
    git clone https://github.com/CiscoDevNet/webex-teams-jwt-samples.git
    cd webex-teams-jwt-samples
    ```

- Install Node.JS dependencies:

    ```shell
    npm install
    ```

- (Optional) create and activate a Python3 virtual environment:

    ```shell
    python3 -m venv venv
    source env/bin/activate
    ```

- Install Python3 dependencies:

    ```shell
    pip install -r requirements.txt
    ```

- Launch Visual Studio Code:

    ```shell
    code .
    ```

- In VS Code:

    1. Rename the file `.env.sample` to `.env`
    
        Edit the `.env` file:

        - Paste in your Webex Teams Guest Issuer ID and shared secret

        - Be sure to save the file

        >Alternatively: use environment variables to specify `WEBEX_TEAMS_ISSUER_ID` and `WEBEX_TEAMS_ISSUER_SECRET`

    1. Open the sample `.js` or `.py` file you wish to run.
    
        From the **Run** panel on the left, select either **Launch Node.js sample** or **Launch Python sample** as appropriate, then either press **F5** or click the green 'Run' button

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/webex-teams-jwt-samples)