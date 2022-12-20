import logging as logger
import pprint
from behave import step, then
import pdb
from helpers.uitilities_helpers import UtilitiesHelper
from helpers.backend_helpers import BackendHelper


@step("I call the '{endpoint}' users api to '{method}'")
def call_create_user_api(context, endpoint, method):
    """

    :param context:
    :param endpoint: The endpoint that is going to be used
    :param method: This defines if the step will be used to create or to update
    :return: It works for both scenarios create and update user. The complete @users scenario
    is to create a user and then update it with the given id
    """
    random_name = UtilitiesHelper().generate_random_first_and_last_name()
    name = random_name['f_name']
    context.parameters = {
        "name": name,
        "job": "QA Engineer"
    }
    # This case applies when creating the user
    if method == "create":
        response = BackendHelper().post(wc_endpoint=endpoint, params=context.parameters, expected_status_code=201)
    # This case applies when updating the user
    else:
        endpoint_with_id = endpoint + "/" + context.created_user_id
        response = BackendHelper().put(wc_endpoint=endpoint_with_id, params=context.parameters,
                                       expected_status_code=200)
    context.response_body = response["response_body"]
    context.status_code = response["status_code"]
    context.headers = response["response_headers"]
    try:
        context.created_user_id = str(context.response_body['id'])
    except:
        logger.info("In this case there is no id, since the scenario is to update "
                    "and the response body does not have this parameter")
    context.endpoint = endpoint


@step("I call the '{endpoint}' register api with '{email}' email and '{password}' password")
def call_create_user_api(context, endpoint, email, password):
    """

    :param context:
    :param endpoint: Endpoint to be call
    :param email: It works to verify if there is a valid or an invalid email
    :param password: It works to verify if there is a valid or an invalid password
    :return: This step works for registering users in three cases, valid data, invalid user and invalid password
    """

    # This case applies for a valid email
    utilities_methods = UtilitiesHelper()
    if email == "valid":

        context.chosen_email = utilities_methods.select_valid_random_email()
        expected_status_code = 200
    # This case applies for the invalid user creation, with a non-registered email
    else:
        context.chosen_email = utilities_methods.generate_random_email_and_password()['email']
        expected_status_code = 400

    # This case applies for a valid password
    if password == "valid":
        random_password = utilities_methods.generate_random_email_and_password()['password']
    # This case applies for an invalid password
    else:
        random_password = ""
        expected_status_code = 400

    logger.info("Used email and password {} and {}".format(context.chosen_email, random_password))
    context.parameters = {
        "email": context.chosen_email,
        "password": random_password
    }
    response = BackendHelper().post(wc_endpoint=endpoint, params=context.parameters,
                                    expected_status_code=expected_status_code)
    context.response_body = response["response_body"]
    context.status_code = response["status_code"]
    context.headers = response["response_headers"]
    try:
        context.created_user_id = str(context.response_body['id'])
    except:
        logger.info("In this case there is no id, since there is an invalid scenario")
    context.endpoint = endpoint


@step("I review the response body, status,and headers")
def i_review_response_body_status_and_headers(context):
    """

    :param context:
    :return: Prints response body
    """

    logger.info(f"the following is the response body of calling {context.endpoint} endpoint:")
    pprint.pprint(context.response_body)
    logger.info(f"with status code: {context.status_code}")
    logger.info("And headers:")
    pprint.pp(context.headers)


@then("the status should be '{expected_status}'")
def status_should_be(context, expected_status):
    """

    :param context:
    :param expected_status:
    :return: Verifies Status code is as expected
    """
    assert int(context.status_code) == int(expected_status), f"Error! Expected Status code " \
                                                             f"{expected_status}. Real Status: {context.status_code}"


@step("I call the '{endpoint}' api with the last created user")
def i_call_the_get_user_api_with_last_created_user(context, endpoint):
    """

    :param context:
    :param endpoint: Endpoint to be call
    :return: This step gets a user with a specific id of the last registered user
    """
    context.endpoint = endpoint + context.created_user_id
    response = BackendHelper().get(wc_endpoint=context.endpoint, expected_status_code=200)
    context.response_body = response["response_body"]
    context.status_code = response["status_code"]


@then("the response body should have the name and job of the created user")
def response_body_should_have_name_and_job_of_created_user(context):
    """

    :param context:
    :return: This step verifies that the gotten user is the same one that was registered at the beginning
    """
    expected_email_with_id = context.chosen_email
    real_email_with_id = context.response_body['data']['email']

    assert expected_email_with_id == real_email_with_id, f"Returned email with created id is not the same " \
                                                         f"as expected. Expected: {expected_email_with_id}. Real: {real_email_with_id}"


@then("the error should be '{expected_error}'")
def the_error_should_be(context, expected_error):
    """

    :param context:
    :param expected_error: This is the expected error
    :return: Verifies that the error is the one expected from the api
    """
    real_error = context.response_body['error']
    assert real_error == expected_error, f"Real and expected error are not the same. " \
                                         f"Expected: {expected_error}. Real: {real_error}"
