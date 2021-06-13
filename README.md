# Bynder UI Testing Assignment
## Description
The app tests login feature in the page https://wave-trial.getbynder.com/login/


## Tech Stack
- Python  
- Pytest  
- Selenium webdriver  
- Docker
- Travis CI

## Test scenarios
- User can log in and log out successfully with valid username and password (passed)
- User can not log in with non-existing username and existing password (passed)
- User can not log in with existing username and non-existing password (passed)
- User can not log in with non-existing username and non-existing password (passed)
- User can not log in with existing username and empty password (passed)
- User can not log in with non-existing username and empty password (passed)
- User can not log in with empty username and empty password (passed)
- User can not log in with empty username and existing password (passed)
- User can not log in with empty username and non-existing password (passed)
- Password field is marked and username field is not marked in login page (passed)
- User can press enter key to log in successfully with valid username and password (passed)
- User is still on dash board page by clicking back button in browser after logging in to dashboard page (passed)
- User is still on login page by clicking back button in browser after logging out to login page (passed)
- User can update password by clicking lost password link (passed)

## Running the test
### Prerequites
in linux system  
docker is installed

### Commands:
- $ sudo docker build -t ui_test .
- $ sudo docker run -v "$PWD":/report/ ui_test

All the commands should be executed in the root directory of the repo. A html test report is generated for the testing. The repo is
also added to Travis CI and is test is executed automatically.