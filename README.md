# APIJuniorChallenge
READ ME:

PREREQUESITES:

The following libraries have to be installed to run tests:
Behave
Selenium
Requests

UNDERSTANDING FOLDERS

You will find a principal folder called APIJuniorChallenge.
In there you will have another folder called Backend_Tests_REQRES and Helpers.
Inside of Helpers folder you will find to python scripts: BackendHelpers and UtilitiesHelpers which are going to be used for different functions that are going to be repeated during the different scenarios.

Into the Backend_Tests_REQRES folders you will have to folders with different scenarios, one of them called Jokes and the other one User.

Users FOLDER:
In this folder, we have a users_and_register.feature with the different scenarios that will be tested
In this folder, we have a steps folder which have a users_steps python script where the different steps are defined.

In order to run users test scenarios you can use the following command:

behave Backend_Tests_REQRES/Users --no-capture -f plain -t “tag_name”


Jokes FOLDER:
n this folder, we have a jokes.feature with the different scenarios that will be tested
In this folder, we have a steps folder which have a jokes_steps python script where the different steps are defined.

In order to run jokes test scenarios you can use the following command:

behave Backend_Tests_REQRES/Jokes --no-capture -f plain -t “tag_name”

Note: It is important to use the —no-capture and -f plain so that all the different informational prints from the tests are successfully printed.

SCENARIOS:

User SCENARIOS:

Scenario: Verify creating random user with 'POST /users' creates a new user, after that update it with 'PUT /users/{id}’

Scenario: Verify 'POST /register' creates a new user with valid user and 'GET /users/{id}'
get a information about the created user

Scenario: Verify 'POST /register' shows error message when creating a non valid user

Scenario: Verify 'POST /register' shows error message when creating a valid user without a password

Jokes SCENARIOS:

Scenario: Verify 'POST /jokes-parade/' creates a new joke

DOCUMENTATION:
There are different commentaries and docstrings in every function so that the code is easy to follow, if you have any doubt don’t hesitate to ask.
