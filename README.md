# webex-teams-jwt-samples

Python and JavaScript sample project for [Visual Studio Code](https://code.visualstudio.com/) showing how to build and authenticate JSON Web Tokens for Cisco Webex Teams.  

Includes 'native' and popular-library examples ([PyJWT](https://pyjwt.readthedocs.io/en/latest/) / [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken))

See background information on the Webex Teams [Guest Issuer](https://developer.webex.com/guest-issuer.html) feature

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
    python3 -m venv env
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

    1. Edit the `.env` file:

        - Paste in your Webex Teams Guest Issuer ID and shared secret (save the file)

        - Be sure to save the file

        >Alternatively: use environment variables to specify `WEBEX_TEAMS_ISSUER_ID` and `WEBEX_TEAMS_ISSUER_SECRET`

    1. Open the sample `.js` or `.py` file you wish to run, and launch by pressing --F5--, or by opening the Debugging panel and clicking the green 'Run' button

