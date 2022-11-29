import random
import pprint
from behave import step, when
import pdb
from Helpers.BackendHelpers import BackendHelper
from Helpers.UtilitiesHelpers import UtilitiesHelper


@step("I call the '{endpoint}' api")
def i_call_jokes_api(context, endpoint):
    """

    :param context:
    :param endpoint: Endpoint used for the call
    :return: Calls /users endpoint and saves response body, status code and id
    """
    context.random_setup = UtilitiesHelper().generate_random_lorem_ipsum()
    context.random_punchline = UtilitiesHelper().generate_random_lorem_ipsum()
    types_list = ["Python", "Java", "C", "C++", "JavaScript", "SQL", "PHP", "GO", "R",
                  "Matlab", "Swift", "Ruby", "Scala"]
    context.random_type = random.choice(types_list)
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
    print("       ")
    print(f"the following is the response body of calling {context.endpoint} endpoint:")
    pprint.pprint(context.response_body)
    print(f"with status code: {context.status_code}")
    print("And headers:")
    pprint.pp(context.headers)
    print("       ")


@step("I should see status '{expected_status}' created")
def i_should_see_status_201_created(context, expected_status):
    """

    :param context:
    :return: Verifies status code
    """

    if int(context.status_code) == int(expected_status):
        print(f"Expected Status code {expected_status}. Real Status: {context.status_code}")
    else:
        raise Exception(f"Error! Expected Status code {expected_status}. Real Status: {context.status_code}")


@step("the response body should be in accordance with the created data")
def response_body_should_be_in_accordance_with_created_data(context):
    """

    :param context:
    :return: Uses three assertions to confirm that created data is correct
    """
    context.execute_steps(u"""
            When Assert type is as created
            When Assert setup is as created
            When Assert punchline is as created
    """)
    print(f"Type, setup and punchline are the same as created before")


@when("Assert type is as created")
def assert_type_is_as_created(context):
   """

   :param context:
   :return: This step is one of the assertions to be called in response_body_should_be_in_accordance_with_created_data
   """
   expected_type = context.random_type
   real_type = context.response_body['type']

   assert expected_type == real_type, f"Expected type is not the same as the real one. " \
                                      f"Expected {expected_type}. Real {real_type}"


@when("Assert setup is as created")
def assert_setup_is_as_created(context):
    """

    :param context:
    :return: This step is one of the assertions to be called in response_body_should_be_in_accordance_with_created_data
    """

    expected_setup = context.random_setup
    real_setup = context.response_body['setup']

    assert expected_setup == real_setup, f"Expected setup is not the same as the real one. " \
                                         f"Expected {expected_setup}. Real {real_setup}"


@when("Assert punchline is as created")
def assert_punchline_is_as_created(context):
    """

    :param context:
    :return: This step is one of the assertions to be called in response_body_should_be_in_accordance_with_created_data
    """

    expected_punchline = context.random_punchline
    real_punchline = context.response_body['punchline']
    assert expected_punchline == real_punchline, f"Expected punchline is not the same as the real one. " \
                                                 f"Expected {expected_punchline}. Real {real_punchline}"
