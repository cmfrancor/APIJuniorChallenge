# Project Name: APIJuniorChallenge

## Description: 
This project was made for learning purposes. It was made using BDD with behave to automate some backend 
tests of the following API: [reqres](https://reqres.in/api)

## Requirements: 
The project code has been developed using Python 3 language.
In addition, the following libraries have to be installed to run tests
- Behave
- Selenium
- Requests


## Installation:
In case you have not installed the libraries, you can use the following commands from your terminal:
```
pip install behave 

pip install selenium

pip install requests
```

After installing the libraries, you can verify that the installation was successful using the following command:
pip freeze
There you will see a list of all your libraries and versions, you should see the three required libraries in that list.

## Usage:
You will find a main folder called api_junior_challenge.
Inside you will have another folder called backend_tests and helpers.
Inside of helpers folder you will find two python scripts: backend_helpers and utilities_helpers 
which contain useful methods that will be constantly used.
For example, backend_helpers has the get, post, put and delete methods to make API calls.
On the other hand, utilities_helpers have different methods to generate random emails and passwords, 
names and lastnames, etc.

Into the tests folders you will have two folders with different scenarios, one of them called 
Jokes and the other one User.

### User folder:
- In this folder, we have a users_and_register.feature with the different scenarios that will be tested
- In this folder, we have a steps folder which have a users_steps python script where the different steps are defined.

In order to run users test scenarios you can use the following command:
```
behave tests/users --no-capture --no-logcapture -f plain -t “tag_name”
```

### Jokes FOLDER:
- In this folder, we have a jokes.feature with the different scenarios that will be tested
- In this folder, we have a steps folder which have a jokes_steps python script where the different steps are defined.

In order to run jokes test scenarios you can use the following command:
```
behave tests/jokes --no-capture --no-logcapture -f plain -t “tag_name”
```


#### Note:
It is important to use the —-no-capture, --no-logcapture and -f plain so that all the different informational
prints from the tests are successfully printed.


## Support:
There are different commentaries and docstrings in every function so that the code is easy to follow.
If you have any doubt don’t hesitate to write to the following mail: mauricio.franco@koombea.com





