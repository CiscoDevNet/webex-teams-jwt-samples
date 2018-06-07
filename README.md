# webex-teams-jwt-samples

Python and JavaScript sample project for [Visual Studio Code](https://code.visualstudio.com/) showing how to build and authenticate JSON Web Tokens for Cisco Webex Teams.  

Includes 'native' and popular-library examples ([PyJWT](https://pyjwt.readthedocs.io/en/latest/) / [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken))

See background information on the Webex Teams [persistent guest issuer](https://developer.webex.com/guest-issuer.html) feature

## Getting Started

* Clone this repo:
    ```shell
    git clone https://github.com/CiscoDevNet/webex-teams-jwt-samples.git
    ```
* Install Node.JS dependencies:
    ```shell
    npm install
    ```
* Put guest issuer id/secret in `secrets.json`
* Be sure to launch the .py and .js files with the appropriate VS Code launch config
