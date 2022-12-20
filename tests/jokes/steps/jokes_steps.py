import pprint
from behave import step, then
import pdb
from helpers.backend_helpers import BackendHelper
from helpers.uitilities_helpers import UtilitiesHelper
import logging as logger


@step("I call the '{endpoint}' api")
def i_call_jokes_api(context, endpoint):
    """

    :param context:
    :param endpoint: Endpoint used for the call
    :return: Calls /users endpoint and saves response body, status code and id
    """
    utilities_methods = UtilitiesHelper()
    context.random_setup = utilities_methods.generate_random_lorem_ipsum()
    context.random_punchline = utilities_methods.generate_random_lorem_ipsum()
    context.random_type = utilities_methods.generate_random_type()

    context.parameters = {
        "type": context.random_type,
        "setup": context.random_setup,
        "punchline": context.random_punchline
    }

    response = BackendHelper().post(wc_endpoint=endpoint, params=context.parameters, expected_status_code=201)
    context.response_body = response["response_body"]
    context.status_code = response["status_code"]
    context.headers = response["response_headers"]
    context.created_user_id = context.response_body['id']
    context.endpoint = endpoint


@step("I review the response body, status,and headers")
def i_review_the_response_body_status_and_headers(context):
    """

        :param context:
        :return: Prints response body
        """
    logger.info(f"the following is the response body of calling {context.endpoint} endpoint:")
    pprint.pprint(context.response_body)
    logger.info(f"with status code: {context.status_code}")
    logger.info("And headers:")
    pprint.pprint(context.headers)


@then("I should see status '{expected_status}' created")
def i_should_see_status_201_created(context, expected_status):
    """

    :param context:
    :param expected_status:
    :return:
    """

    if int(context.status_code) == int(expected_status):
        logger.info(f"Expected Status code {expected_status}. Real Status: {context.status_code}")
    else:
        raise Exception(f"Error! Expected Status code {expected_status}. Real Status: {context.status_code}")


@then("the response body should be in accordance with the created data")
def response_body_should_be_in_accordance_with_created_data(context):
    """

    :param context:
    :return: Uses three assertions to confirm that created data is correct
    """
    context.execute_steps(u"""
            Then verify type is as created
            Then verify setup is as created
            Then verify punchline is as created
    """)
    logger.info("Type, setup and punchline are the same as created before")


@then("verify type is as created")
def verify_type_is_as_created(context):
    """

   :param context:
   :return: This step is one of the assertions to be called in response_body_should_be_in_accordance_with_created_data
   """
    expected_type = context.random_type
    real_type = context.response_body['type']

    assert expected_type == real_type, f"Expected type is not the same as the real one. " \
                                       f"Expected {expected_type}. Real {real_type}"


@then("verify setup is as created")
def verify_setup_is_as_created(context):
    """

    :param context:
    :return: This step is one of the assertions to be called in response_body_should_be_in_accordance_with_created_data
    """

    expected_setup = context.random_setup
    real_setup = context.response_body['setup']

    assert expected_setup == real_setup, f"Expected setup is not the same as the real one. " \
                                         f"Expected {expected_setup}. Real {real_setup}"


@then("verify punchline is as created")
def verify_punchline_is_as_created(context):
    """

    :param context:
    :return: This step is one of the assertions to be called in response_body_should_be_in_accordance_with_created_data
    """

    expected_punchline = context.random_punchline
    real_punchline = context.response_body['punchline']
    assert expected_punchline == real_punchline, f"Expected punchline is not the same as the real one. " \
                                                 f"Expected {expected_punchline}. Real {real_punchline}"
